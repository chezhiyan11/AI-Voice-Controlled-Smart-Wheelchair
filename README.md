<div align="center">

# ♿ AI-Powered Intelligent Voice-Controlled Smart Wheelchair

### Empowering Mobility Through Artificial Intelligence, Embedded Systems & IoT

<img src="images/banner.png" width="100%"/>

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4-red?style=for-the-badge&logo=raspberrypi)
![ESP32](https://img.shields.io/badge/ESP32-IoT-orange?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow)
![Vosk](https://img.shields.io/badge/Vosk-Speech%20Recognition-purple?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

---

### 🚀 AI • Embedded Systems • Computer Vision • Speech Recognition • IoT

</div>

---

# 📖 Overview

Millions of people worldwide experience mobility challenges due to paralysis, lower-limb disabilities, and visual impairments. Traditional wheelchairs require manual effort or expensive automation, making independent movement difficult.

This project introduces an **AI-powered intelligent wheelchair** capable of understanding **voice commands**, detecting **real-time obstacles**, and making **autonomous navigation decisions** using **Artificial Intelligence, Computer Vision, and Embedded Systems**.

The wheelchair processes offline speech commands using **Vosk Speech Recognition**, identifies surrounding objects through **OpenCV + TensorFlow**, and communicates with an **ESP32 motor controller** to execute safe movement.

The objective is to provide a **low-cost**, **accessible**, and **intelligent mobility solution** that significantly improves independence and quality of life.

---

# 🎯 Project Highlights

✅ Offline Voice Recognition

✅ AI-Based Navigation

✅ Vision-Based Obstacle Detection

✅ Autonomous Decision Making

✅ Embedded Motor Control

✅ Raspberry Pi + ESP32 Integration

✅ IoT Communication

✅ Affordable Assistive Technology

---

# ✨ Key Features

🎙 **Voice Controlled Navigation**

- Forward
- Backward
- Left
- Right
- Stop

---

🧠 **Offline Speech Recognition**

- Vosk Speech Recognition
- Speech-to-Text Conversion
- Keyword Spotting
- Low Latency
- No Internet Required

---

👁 **Computer Vision**

- OpenCV
- TensorFlow
- MobileNet SSD
- Object Detection
- Path Identification
- Obstacle Recognition

---

🚧 **Obstacle Detection**

- Ultrasonic Sensors
- IR Sensors
- Real-Time Distance Measurement
- Automatic Collision Avoidance

---

⚙ **Embedded Control**

- ESP32
- UART Communication
- Raspberry Pi GPIO
- Motor Driver Control

---

🔋 **Smart Navigation**

- AI Decision Making
- Autonomous Path Selection
- Safe Turning
- Emergency Stop

---

# 🏗 System Architecture

```text
                                       USER
                                        │
                                        ▼
                              Voice Command Input
                                        │
                                        ▼
                          ReSpeaker 2-Mic HAT (Audio Capture)
                                        │
                                        ▼
                          Raspberry Pi 4 Controller (Linux OS)
                                        │
            ┌───────────────────────────┴───────────────────────────┐
            │                                                       │
            ▼                                                       ▼
 ┌───────────────────────────┐                        ┌────────────────────────────┐
 │ Voice Recognition Module  │                        │ Computer Vision Module     │
 ├───────────────────────────┤                        ├────────────────────────────┤
 │ • Vosk Speech-to-Text     │                        │ • Camera Module 3 NoIR     │
 │ • Keyword Spotting (KWS)  │                        │ • OpenCV                   │
 │ • Command Parsing         │                        │ • TensorFlow               │
 │                           │                        │ • MobileNet SSD            │
 └───────────────┬───────────┘                        └───────────────┬────────────┘
                 │                                                    │
                 │                                                    │
                 └──────────────────────┬─────────────────────────────┘
                                        ▼
                          ┌─────────────────────────────┐
                          │   AI Decision Manager       │
                          ├─────────────────────────────┤
                          │ • Voice Command Validation  │
                          │ • Object Detection          │
                          │ • Path Recognition          │
                          │ • Obstacle Avoidance        │
                          │ • Navigation Decision       │
                          └──────────────┬──────────────┘
                                         │
                                         ▼
                         ┌──────────────────────────────┐
                         │ ESP32 Embedded Controller    │
                         ├──────────────────────────────┤
                         │ • Motor Control Logic        │
                         │ • Sensor Monitoring          │
                         │ • PWM Generation             │
                         │ • Safety Override            │
                         └──────────────┬───────────────┘
                                        │
                ┌───────────────────────┼────────────────────────┐
                │                       │                        │
                ▼                       ▼                        ▼
      Ultrasonic Sensors         IR Sensors            L298N Motor Driver
                │                       │                        │
                └───────────────┬───────┴───────────────┬────────┘
                                ▼
                       Wheelchair Motion Control
                                │
                                ▼
         Forward • Backward • Left • Right • Stop
```
---

# 🧠 AI Workflow

```
┌────────────────────────────────────────────┐
│         Camera Module 3 NoIR               │
│      Real-Time Video Frame Capture         │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│         Frame Acquisition                  │
│ • Continuous Image Capture                 │
│ • Video Stream Generation                  │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      Image Preprocessing (OpenCV)          │
│ • Resize Frames                            │
│ • Noise Reduction                          │
│ • Image Enhancement                        │
│ • Frame Normalization                      │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│     Deep Learning Inference                │
│         MobileNet SSD                      │
│ • Object Detection                         │
│ • Object Classification                    │
│ • Confidence Estimation                    │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│       Environment Analysis                 │
│ • Obstacle Localization                    │
│ • Free Path Identification                 │
│ • Safe Zone Detection                      │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│       AI Decision Engine                   │
│ • Path Planning                            │
│ • Collision Avoidance                      │
│ • Movement Decision                        │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      Navigation Command Generation         │
│ • Forward                                  │
│ • Left                                     │
│ • Right                                    │
│ • Stop                                     │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│        ESP32 Motor Controller              │
│ • Motion Execution                         │
│ • PWM Motor Control                        │
└────────────────────────────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│       Autonomous Wheelchair Movement       │
└────────────────────────────────────────────┘
```

---

# 🎤 Voice Recognition Pipeline

```
                 VOICE RECOGNITION PIPELINE

┌────────────────────────────────────────────┐
│            User Voice Command              │
│   (Forward / Left / Right / Stop)          │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      ReSpeaker 2-Mic HAT                   │
│      Audio Capture & Noise Reduction       │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      Audio Preprocessing                   │
│ • Echo Cancellation                        │
│ • Noise Suppression                        │
│ • Voice Signal Enhancement                 │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      Vosk Speech Recognition Engine        │
│      Offline Speech-to-Text (STT)          │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      Command Interpretation                │
│ • Keyword Spotting (KWS)                   │
│ • Command Validation                       │
│ • Intent Recognition                       │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│      AI Decision Manager                   │
│ • Verify Safe Movement                     │
│ • Combine Vision & Sensor Data             │
│ • Generate Navigation Command              │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│        ESP32 Motor Controller              │
│ • Motion Control                           │
│ • PWM Generation                           │
│ • Safety Override                          │
└────────────────────┬───────────────────────┘
                     │
                     ▼
┌────────────────────────────────────────────┐
│       Autonomous Wheelchair Movement       │
│  Forward • Left • Right • Stop             │
└────────────────────────────────────────────┘
```

---

# 🛠 Hardware Components

| Component | Purpose |
|------------|-----------|
| Raspberry Pi 4 | Main AI Processing Unit |
| ESP32 | Motor Controller |
| ReSpeaker 2-Mic HAT | Voice Input |
| Raspberry Pi Camera Module 3 NoIR | Computer Vision |
| Ultrasonic Sensors | Obstacle Detection |
| IR Sensors | Short Range Detection |
| L298N Motor Driver | Motor Control |
| BO Motors | Wheelchair Movement |
| Battery Pack | Power Supply |
| Voltage Regulator | Stable Power |

---

# 💻 Software Stack

| Technology | Purpose |
|-------------|----------|
| Python | AI Programming |
| OpenCV | Computer Vision |
| TensorFlow | Deep Learning |
| MobileNet SSD | Object Detection |
| Vosk | Offline Speech Recognition |
| Arduino IDE | ESP32 Programming |
| Raspberry Pi OS | Embedded Operating System |
| UART | Communication |
| GPIO | Hardware Interface |

---

# 📂 Repository Structure

```
AI-Voice-Controlled-Smart-Wheelchair

│

├── Images/

├── Hardware/

├── Software/

│      ├── RaspberryPi/

│      ├── ESP32/

│

├── AI_Model/

├── Documentation/

├── Demo/

├── README.md

├── requirements.txt

└── LICENSE
```

---

# 🚀 Installation

Clone Repository

```bash
git clone https://github.com/chezhiyan11/AI-Voice-Controlled-Smart-Wheelchair.git
```

Move to Project

```bash
cd AI-Voice-Controlled-Smart-Wheelchair
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Run

```bash
python main.py
```

---

# 🎮 Voice Commands

| Voice Command | Action |
|---------------|--------|
| Forward | Move Forward |
| Backward | Move Backward |
| Left | Turn Left |
| Right | Turn Right |
| Stop | Stop Movement |

---

# 📊 Working Principle

1. User speaks a voice command.

2. ReSpeaker captures the speech.

3. Vosk converts speech into text.

4. Raspberry Pi interprets the command.

5. Camera continuously detects obstacles.

6. AI analyzes surroundings.

7. Raspberry Pi sends movement instructions.

8. ESP32 controls motors.

9. Wheelchair moves safely.

---

# 📸 Project Demonstration

## Prototype

<img src="images/Prototype visualization.png"/>

---

## Block Diagram

<img src="images/Block Diagram.jpeg"/>

---


# 📈 Results

✔ Successful Offline Speech Recognition

✔ Real-Time Object Detection

✔ Autonomous Navigation

✔ Embedded Motor Control

✔ Low Latency Response

✔ Collision Avoidance

✔ Affordable Smart Mobility Solution

---

# 🔮 Future Enhancements

- YOLOv11 Object Detection
- SLAM Navigation
- GPS Tracking
- Android Application
- Emergency SOS
- Health Monitoring
- Cloud Connectivity
- Face Recognition
- Voice Authentication
- Indoor Mapping

---

# 🤝 Contributors

| Name |
|------|
| Chezhiyan M |
| Anish S |
| Subramanian M |
| Adithya R |

---

# 🏆 Achievements

🏅 Developed for **Unisys Innovation Program**

🏅 AI-Based Embedded Healthcare Innovation

🏅 Real-Time Computer Vision Application

🏅 Assistive Technology Prototype

---

# 📜 License

This project is licensed under the MIT License.

---

<div align="center">

## ⭐ If you like this project, consider giving it a Star!

Made with ❤️ by **Chezhiyan M & Team**

</div>
