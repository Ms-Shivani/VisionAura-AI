# 👁️ VisionAura AI — EDITH Face Detection Module

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv"/>
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Team-Hackronauts-orange?style=for-the-badge"/>
</p>

> **Real-time face & eye detection system** built as part of the VisionAura AI project — an AI-powered computer vision platform for object detection and surveillance.

---

## 🚀 What It Does

| Feature | Description |
|---|---|
| 👤 Face Detection | Real-time multi-face detection via webcam |
| 👁️ Eye Detection | Detects eyes within each identified face |
| 📊 FPS Counter | Live frames-per-second performance display |
| 📸 Screenshot | Press `S` to capture and save any frame |
| 🖥️ UI Overlay | Clean on-screen display with face count badge |

---

## 🎯 Demo

```
[EDITH] Starting webcam...
[INFO]  Detection running. Press Q to quit, S for screenshot.
[EDITH] Faces Detected: 2  |  FPS: 28.4
[EDITH] Screenshot saved: screenshots/edith_capture_20240623_143022.jpg
```

---

## 🛠️ Tech Stack

- **Python 3.8+**
- **OpenCV** — computer vision & Haar Cascade classifiers
- **NumPy** — image matrix operations

---

## ⚙️ Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/Ms-Shivani/VisionAura-AI.git
cd VisionAura-AI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the module
```bash
python face_detection.py
```

### Controls
| Key | Action |
|---|---|
| `S` | Save screenshot |
| `Q` | Quit the program |

---

## 📁 Project Structure

```
VisionAura-AI/
│
├── face_detection.py      # Main detection module
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── screenshots/           # Auto-created on first capture
```

---

## 💡 How It Works

1. **Webcam feed** is captured frame-by-frame using OpenCV
2. Each frame is converted to **grayscale** and histogram-equalized for better accuracy
3. **Haar Cascade classifier** scans for face regions using sliding window detection
4. Within each detected face ROI, a second cascade detects **eyes**
5. Bounding boxes, labels, and UI elements are drawn on the **color frame**
6. Final frame is displayed in real-time at 25–30 FPS

---

## 🌐 About VisionAura AI

VisionAura AI is a full-stack AI-powered computer vision platform built by **Team Hackronauts** for real-time:
- Object detection & classification
- Face recognition & surveillance
- Emotion analysis (upcoming)

This repository contains the **EDITH Face Detection Module** — the core perception layer of the system.

---

## 👩‍💻 Author

**Shivani** | BE CSE | Chitkara University  
📌 [LinkedIn](https://www.linkedin.com/in/ms-shivani-7ab502383) | [GitHub](https://github.com/Ms-Shivani)

*Built with ❤️ by Team Hackronauts*
