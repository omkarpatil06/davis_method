import os
import cv2
import numpy as np

def extract_frames(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return []
    frames = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frames.append(gray_frame)
        frame_count += 1
    cap.release()
    print(f"Extracted {frame_count} frames.")
    return np.array(frames)

def get_video_info(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise IOError("Could not open video file")

    # Get video information
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = frame_count / fps
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    ret, frame = cap.read()
    if not ret:
        raise IOError("Could not read frame from video")

    channels = frame.shape[2] if len(frame.shape) == 3 else 1
    cap.release()
    return {
        "duration": duration,
        "fps": fps,
        "width": width,
        "height": height,
        "channels": channels
    }