# video_processing/emotion_detection.py

import cv2
from deepface import DeepFace

def detect_emotion_from_frame(frame):
    """Analyze facial emotion from a single frame."""
    try:
        analysis = DeepFace.analyze(frame, actions=['emotion'])
        return analysis['dominant_emotion']
    except Exception as e:
        return str(e)

def analyze_emotions(video_file):
    """Process video and analyze emotions frame by frame."""
    cap = cv2.VideoCapture(video_file)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        emotion = detect_emotion_from_frame(frame)
        print(f"Detected emotion: {emotion}")
    
    cap.release()

if __name__ == "__main__":
    analyze_emotions('path/to/video/file.mp4')
