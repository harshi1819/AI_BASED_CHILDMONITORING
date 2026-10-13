# child_monitoring_project

# 👶 AI-Based Infant Monitoring System

### A Multi-Modal Infant Distress Detection Framework Using Audio-Visual Fusion and IoT-Based Alerting

## 📌 Project Overview

This project presents an AI-assisted infant monitoring prototype designed to help caregivers identify potential infant distress through audio analysis, facial expression analysis, and automated SMS notifications.

The system combines audio signal processing and computer vision to detect cry-like sounds, analyze facial expressions, and apply decision-making logic to determine when a caregiver alert should be triggered.

The prototype demonstrates how Python, AI-based facial analysis, and cloud-based messaging can be integrated into an infant-monitoring workflow.

## 🎯 Objectives

- Detect cry-like sounds using audio signal features.
- Analyze facial expressions using computer vision.
- Combine audio and visual information for alert decisions.
- Send SMS notifications to caregivers using the Twilio API.
- Integrate multiple modules into a working monitoring prototype.

## ⚙️ Key Features

- **Audio-Based Cry Detection:** Uses Root Mean Square (RMS) energy and audio signal features to identify cry-like sounds.
- **Facial Expression Analysis:** Uses DeepFace to analyze facial expressions captured through a webcam.
- **Audio-Visual Fusion:** Combines audio detection and facial analysis through decision-making logic.
- **SMS Notifications:** Uses Twilio to send alerts to configured phone numbers.
- **Concurrent Processing:** Uses multithreading to coordinate audio and video processing.
- **Real-Time Prototype:** Integrates the monitoring components into a single application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application development |
| OpenCV | Webcam and video processing |
| NumPy | Numerical and audio signal calculations |
| sounddevice | Audio input and recording |
| DeepFace | Facial expression analysis |
| Twilio API | SMS notifications |
| Multithreading | Concurrent audio/video processing |
| Git & GitHub | Version control and project hosting |

## 🏗️ System Workflow

1. Capture audio input through a microphone.
2. Process audio windows and calculate signal features such as RMS energy.
3. Identify cry-like sounds using the implemented detection logic.
4. Capture webcam frames and analyze facial expressions using DeepFace.
5. Apply the programmed decision logic to evaluate available audio and visual information.
6. Trigger an SMS notification through Twilio when the configured alert conditions are met.

**Workflow:** Audio Input + Webcam Input → Signal Processing and Facial Analysis → Decision Logic → SMS Alert

## 💻 Installation and Setup

### Prerequisites

- Python version compatible with the project's dependencies
- Visual Studio Code or another Python IDE
- Webcam and microphone
- Internet connection for Twilio SMS functionality
- Twilio account and configured phone numbers

### 1. Clone the repository

```bash
git clone https://github.com/harshi1819/AI_BASED_CHILDMONITORING.git
cd AI_BASED_CHILDMONITORING
```

### 2. Create a virtual environment

On Windows:

```powershell
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

If the repository contains a `requirements.txt` file:

```bash
python -m pip install -r requirements.txt
```

Otherwise, install the dependencies documented for the project.

### 4. Configure Twilio credentials

Set the following environment variables using your own Twilio account details:

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_PHONE_NUMBER`
- `PARENT_PHONE_NUMBER`

Never commit real credentials, authentication tokens, or private phone numbers to GitHub.

### 5. Run the application

If `final_monitor.py` is the main application script:

```bash
python final_monitor.py
```

Ensure the required dependencies, webcam, microphone, and environment variables are configured before running the application.

## 👩‍💻 My Contribution

As part of a four-member team, I contributed to the core development and integration of the project, including:

- Audio-based cry-like sound detection using RMS energy and audio signal features.
- Integration of DeepFace for facial expression analysis.
- Development of audio-visual decision-making logic.
- Integration of Twilio SMS notifications.
- Multithreading, debugging, and system integration.

## 🧩 Challenges Faced

- Distinguishing cry-like sounds from background noise.
- Integrating audio processing with webcam-based facial analysis.
- Coordinating concurrent tasks and maintaining system responsiveness.
- Refining alert conditions to reduce unnecessary notifications.
- Resolving software dependency, execution, and integration issues.

## 📊 Project Outcome

The project resulted in a working prototype demonstrating:

- Audio-based cry-like sound detection.
- Webcam-based facial expression analysis.
- Combined decision-making using audio and visual information.
- Automated SMS notification functionality.

Further evaluation is needed to measure detection accuracy, false-alert rates, response time, and reliability under different real-world conditions.

## ⚠️ Limitations

- RMS-based audio detection can be affected by background noise and other loud sounds.
- Facial expression analysis does not reliably establish an infant's medical condition or actual distress.
- Performance depends on lighting, camera placement, microphone quality, and software configuration.
- SMS delivery depends on network availability and Twilio service.
- The prototype is intended for educational and research purposes. It is not a medical device and must not replace direct caregiver supervision.

## 🔬 Future Enhancements

- Train and evaluate a dedicated infant-cry classification model.
- Improve robustness to background noise.
- Evaluate audio and visual fusion using a larger, representative dataset.
- Add configurable alert thresholds and caregiver notifications.
- Test performance, false positives, false negatives, and response time systematically.
- Explore deployment on dedicated edge devices.

## 📜 Innovation and Intellectual Property

The project explores an AI-assisted approach to infant monitoring. Any patent-related claims should reflect the actual application status and verified documentation. A patent application, if filed, does not necessarily mean that a patent has been granted.

## 👥 Team

- Harshitha Busireddy
- Deepthi Thoka
- Keerthika Aswa
- Agnuru Vineetha

## 🙏 Acknowledgements

We sincerely thank our project guide, **Dr. K. E. Srinivasa Murthy Sir**, **Dr. Jayalakshmi M. Madam**, and our project coordinator, **Geetha Rani Madam**, for their guidance, encouragement, and support throughout the project.

## 🔗 Repository

[View the project on GitHub](https://github.com/harshi1819/AI_BASED_CHILDMONITORING)

---

*Developed as a final-year B.Tech Electronics and Communication Engineering project at Ravindra College of Engineering for Women, Kurnool, Andhra Pradesh.*
