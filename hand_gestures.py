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


def fist(landmarks):
    print("a")
    thumb_tip = landmarks.landmark[mphands.HandLandmark.THUMB_TIP]
    index_tip = landmarks.landmark[mphands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks.landmark[mphands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks.landmark[mphands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks.landmark[mphands.HandLandmark.PINKY_TIP]

    distance_thumb_index = calculate_distance(thumb_tip, index_tip)
    distance_index_middle = calculate_distance(index_tip, middle_tip)
    distance_middle_ring = calculate_distance(middle_tip, ring_tip)
    distance_ring_pinky = calculate_distance(ring_tip, pinky_tip)

    if distance_thumb_index < 0.05 and distance_index_middle < 0.05 and distance_middle_ring < 0.05 and distance_ring_pinky < 0.05:
        return True
    
    return False

def calculate_distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2) ** 0.5