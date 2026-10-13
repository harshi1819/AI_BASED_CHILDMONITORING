import cv2
import numpy as np
import pygame
import sounddevice as sd
from scipy.io.wavfile import write
from tensorflow.keras.models import load_model
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

# ------------------------------
# CONFIG
# ------------------------------
MODEL_PATH = "emotion_model.h5"
ALERT_SOUND = "alert.mp3"
AUDIO_FILE = "recorded_alert.wav"

# Twilio SMS
TWILIO_SID = "your_twilio_sid"
TWILIO_AUTH = "your_twilio_auth"
TWILIO_NUM = "+1234567890"
TO_NUM = "+91XXXXXXXXXX"

# Email (use app password if Gmail)
EMAIL_USER = "yourmail@gmail.com"
EMAIL_PASS = "your_app_password"
TO_EMAIL = "receiver@gmail.com"
# ------------------------------

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Load model
model = load_model(MODEL_PATH)
classes = ["Angry", "Happy", "Sad", "Surprise", "Neutral"]

# Init pygame
pygame.mixer.init()

def play_audio_alert():
    """Play immediate alert sound"""
    try:
        pygame.mixer.music.load(ALERT_SOUND)
        pygame.mixer.music.play()
    except Exception as e:
        print("Audio play error:", e)

def record_live_audio(duration=5, fs=44100):
    """Record audio from microphone"""
    print("🎤 Recording live audio...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype="int16")
    sd.wait()
    write(AUDIO_FILE, fs, recording)
    print(f"Saved audio: {AUDIO_FILE}")

def send_sms_alert(label):
    """Send SMS alert"""
    try:
        client = Client(TWILIO_SID, TWILIO_AUTH)
        msg = client.messages.create(
            body=f"⚠️ Child Alert! Emotion: {label}. Check your email for audio recording.",
            from_=TWILIO_NUM,
            to=TO_NUM
        )
        print("SMS sent:", msg.sid)
    except Exception as e:
        print("SMS error:", e)

def send_email_with_audio(label):
    """Send email with recorded audio file"""
    try:
        msg = EmailMessage()
        msg["Subject"] = f"Child Alert - {label}"
        msg["From"] = EMAIL_USER
        msg["To"] = TO_EMAIL
        msg.set_content(f"Child detected with emotion: {label}\nAudio recording attached.")

        with open(AUDIO_FILE, "rb") as f:
            msg.add_attachment(f.read(), maintype="audio", subtype="wav", filename=AUDIO_FILE)

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
        print("📧 Email sent with audio!")
    except Exception as e:
        print("Email error:", e)

# ------------------------------
# MAIN LOOP
# ------------------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        roi = gray[y:y+h, x:x+w]
        roi = cv2.resize(roi, (48, 48)) / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)

        pred = model.predict(roi)
        label = classes[pred.argmax()]

        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Trigger alert
        if label in ["Sad", "Angry"]:
            play_audio_alert()
            record_live_audio(duration=5)   # capture 5 sec
            send_sms_alert(label)
            send_email_with_audio(label)

    cv2.imshow("Child Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()


