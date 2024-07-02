# This code will notice when a thumbs up is detected in the camera feed
import mediapipe as mp

mphands = mp.solutions.hands

def thumbsUp(landmarks):
    thumb_tip = landmarks.landmark[mphands.HandLandmark.THUMB_TIP]
    thumb_ip = landmarks.landmark[mphands.HandLandmark.THUMB_IP]
    thumb_mcp = landmarks.landmark[mphands.HandLandmark.THUMB_MCP]
    thumb_base = landmarks.landmark[mphands.HandLandmark.THUMB_CMC]

    is_thumb_up = (thumb_tip.y < thumb_ip.y < thumb_mcp.y < thumb_base.y) and (abs(thumb_tip.x - thumb_base.x) < 0.1)
    for finger in [mphands.HandLandmark.INDEX_FINGER_TIP, mphands.HandLandmark.MIDDLE_FINGER_TIP, mphands.HandLandmark.RING_FINGER_TIP, mphands.HandLandmark.PINKY_TIP]:
        if landmarks.landmark[finger].y < landmarks.landmark[finger - 2].y:
            return False

    return is_thumb_up