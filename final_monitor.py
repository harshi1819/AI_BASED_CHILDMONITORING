import cv2
import numpy as np
import sounddevice as sd
import time
import threading
from deepface import DeepFace
from twilio.rest import Client

# ================= CONFIG =================

TWILIO_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
FROM_NUM = os.getenv("TWILIO_FROM_NUMBER")
TO_NUM = os.getenv("PARENT_PHONE_NUMBER")

SAMPLE_RATE = 16000
WINDOW = 0.5
RMS_THRESHOLD = 0.01   # lowered for better detection
CONSECUTIVE = 2        # faster detection
COOLDOWN = 30

# ==========================================

client = Client(TWILIO_SID, TWILIO_TOKEN)

latest_emotion = None
face_detected = False
last_sms_time = 0

# ==========================================

def send_sms(msg):
    global last_sms_time
    if time.time() - last_sms_time < COOLDOWN:
        print("Cooldown active")
        return
    try:
        client.messages.create(body=msg, from_=FROM_NUM, to=TO_NUM)
        print("✅ SMS SENT")
        last_sms_time = time.time()
    except Exception as e:
        print("❌ SMS Error:", e)

# ==========================================

def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        return result[0]['dominant_emotion']
    except:
        return None

# ==========================================

def video_thread():
    global latest_emotion, face_detected

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        emotion = detect_emotion(frame)

        if emotion:
            face_detected = True
            latest_emotion = emotion
            cv2.putText(frame, emotion, (20,50),
                        cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        else:
            face_detected = False
            latest_emotion = None

        cv2.imshow("Video Monitor", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# ==========================================

def extract_features(audio):
    rms = np.sqrt(np.mean(audio**2))
    return rms

def classify_sound(audio):
    rms = extract_features(audio)
    print("RMS:", rms)   # DEBUG

    if rms > RMS_THRESHOLD:
        return "CRY"
    else:
        return "NOISE"

# ==========================================

def audio_thread():
    consec = 0

    def callback(indata, frames, time_info, status):
        nonlocal consec

        mono = np.mean(indata, axis=1)
        sound = classify_sound(mono)

        if sound == "CRY":
            consec += 1
        else:
            consec = 0

        if consec >= CONSECUTIVE:
            print("🔊 CRY DETECTED")
            handle_event()
            consec = 0

    with sd.InputStream(channels=1,
                        samplerate=SAMPLE_RATE,
                        blocksize=int(SAMPLE_RATE*WINDOW),
                        callback=callback):
        while True:
            time.sleep(0.1)

# ==========================================

def handle_event():
    global latest_emotion, face_detected

    print("Emotion:", latest_emotion, "| Face:", face_detected)

    # FINAL DECISION LOGIC
    if face_detected:
        if latest_emotion in ["sad", "angry"]:
            send_sms("🚨 Baby is crying and distressed! Check immediately.")
        else:
            print("No distress emotion → No SMS")
    else:
        # IMPORTANT: Cry alone should trigger
        send_sms("🚨 Baby crying detected! Please check.")

# ==========================================

def main():
    t1 = threading.Thread(target=video_thread)
    t2 = threading.Thread(target=audio_thread)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()