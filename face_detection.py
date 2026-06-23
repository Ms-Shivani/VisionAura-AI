"""
VisionAura AI — EDITH Face Detection Module
============================================
Project by: Shivani (Team Hackronauts)
GitHub: github.com/Ms-Shivani

Real-time face detection using OpenCV with:
- Live webcam feed
- Face bounding boxes with confidence display
- Eye detection within detected faces
- FPS counter
- Screenshot capture on keypress
"""

import cv2
import time
import os
from datetime import datetime


def load_cascades():
    """Load Haar Cascade classifiers for face and eye detection."""
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
    return face_cascade, eye_cascade


def draw_detections(frame, faces, gray, eye_cascade):
    """Draw bounding boxes and labels on detected faces and eyes."""
    face_count = len(faces)

    for i, (x, y, w, h) in enumerate(faces):
        # Draw face rectangle
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Label above the box
        label = f"Face {i + 1}"
        cv2.putText(frame, label, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Eye detection inside face ROI
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10)

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (255, 100, 0), 2)

    return frame, face_count


def draw_ui(frame, face_count, fps):
    """Draw UI overlay — title bar, FPS, face count, instructions."""
    h, w = frame.shape[:2]

    # Top banner
    cv2.rectangle(frame, (0, 0), (w, 50), (20, 20, 20), -1)
    cv2.putText(frame, "VisionAura AI  |  EDITH Face Detection", (10, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 220, 255), 2)

    # FPS
    cv2.putText(frame, f"FPS: {fps:.1f}", (w - 130, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 1)

    # Face count badge
    badge_color = (0, 180, 0) if face_count > 0 else (0, 0, 180)
    cv2.rectangle(frame, (10, 60), (210, 90), badge_color, -1)
    cv2.putText(frame, f"Faces Detected: {face_count}", (18, 82),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

    # Bottom instructions
    cv2.rectangle(frame, (0, h - 35), (w, h), (20, 20, 20), -1)
    cv2.putText(frame, "Press S — Screenshot  |  Q — Quit", (10, h - 12),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (180, 180, 180), 1)

    return frame


def save_screenshot(frame):
    """Save current frame as a timestamped screenshot."""
    os.makedirs("screenshots", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"screenshots/edith_capture_{timestamp}.jpg"
    cv2.imwrite(filename, frame)
    print(f"[EDITH] Screenshot saved: {filename}")
    return filename


def run_detection():
    """Main detection loop."""
    print("=" * 50)
    print("  VisionAura AI — EDITH Face Detection Module")
    print("  Team Hackronauts | github.com/Ms-Shivani")
    print("=" * 50)
    print("\n[INFO] Starting webcam...")

    face_cascade, eye_cascade = load_cascades()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("[ERROR] Could not open webcam. Check connection.")
        return

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    prev_time = time.time()
    print("[INFO] Detection running. Press Q to quit, S for screenshot.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Frame capture failed.")
            break

        # FPS calculation
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time + 1e-6)
        prev_time = curr_time

        # Convert to grayscale for detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(60, 60)
        )

        # Draw detections and UI
        frame, face_count = draw_detections(frame, faces, gray, eye_cascade)
        frame = draw_ui(frame, face_count, fps)

        cv2.imshow("VisionAura AI — EDITH", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("[INFO] Shutting down EDITH...")
            break
        elif key == ord('s'):
            save_screenshot(frame)

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Session ended.")


if __name__ == "__main__":
    run_detection()
