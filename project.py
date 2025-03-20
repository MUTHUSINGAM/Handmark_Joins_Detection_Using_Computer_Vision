import cv2
import mediapipe as mp
import streamlit as st
from PIL import Image
import numpy as np

# Initialize MediaPipe Holistic model 
mp_holistic = mp.solutions.holistic
holistic = mp_holistic.Holistic(static_image_mode=False, model_complexity=1, smooth_landmarks=True, enable_segmentation=False, refine_face_landmarks=False)

mp_draw = mp.solutions.drawing_utils

# Dictionary for naming finger tips
FINGER_TIPS = {4: "Thumb", 8: "Index", 12: "Middle", 16: "Ring", 20: "Pinky"}

# Dictionary for naming major body joints
BODY_JOINTS = {
    11: "Left Shoulder", 12: "Right Shoulder",
    13: "Left Elbow", 14: "Right Elbow",
    15: "Left Wrist", 16: "Right Wrist",
    23: "Left Hip", 24: "Right Hip",
    25: "Left Knee", 26: "Right Knee",
    27: "Left Ankle", 28: "Right Ankle"
}


st.title("Hand & Body Joint Tracking (Real-time)")


cap = cv2.VideoCapture(0)


if not cap.isOpened():
    st.error("Error: Unable to access the camera.")
else:
    
    video_placeholder = st.empty()

    while True:
        ret, frame = cap.read()
        if not ret:
            st.error("Error: Unable to read video frame.")
            break

        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = holistic.process(frame_rgb)

        
        if results.right_hand_landmarks:
            mp_draw.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            for idx, landmark in enumerate(results.right_hand_landmarks.landmark):
                if idx in FINGER_TIPS:
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.putText(frame, FINGER_TIPS[idx], (cx, cy - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        if results.left_hand_landmarks:
            mp_draw.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
            for idx, landmark in enumerate(results.left_hand_landmarks.landmark):
                if idx in FINGER_TIPS:
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.putText(frame, FINGER_TIPS[idx], (cx, cy - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        
        if results.pose_landmarks:
            mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS)

            
            for idx, landmark in enumerate(results.pose_landmarks.landmark):
                if idx in BODY_JOINTS:
                    h, w, _ = frame.shape
                    cx, cy = int(landmark.x * w), int(landmark.y * h)
                    cv2.putText(frame, BODY_JOINTS[idx], (cx, cy - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        
        image = Image.fromarray(frame_rgb)
        video_placeholder.image(image, channels="RGB", use_column_width=True)

    cap.release()
