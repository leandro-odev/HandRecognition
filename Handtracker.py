# Library: OpenCV, Mediapipe
import cv2 as cv
import mediapipe as mp
from hand_gestures import thumbsUp, fist

# Initialize MediaPipe drawing utilities and hand tracking module
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

# Start capturing video from the default camera (example: on a laptop is the webcam. if 0 is not working, try 1 and so on, because it depends on the number of cameras connected to the device)
capture = cv.VideoCapture(0)
hands = mphands.Hands()

payet_img = cv.imread('Resources/Payet_thumpsUp.jpg')
spider_fist = cv.imread('Resources/Spider_fist.jpg')
def resize(img, scale=0.75):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(img, dimensions, interpolation = cv.INTER_AREA)

payet_img = resize(payet_img)

while True:
    # Read a frame from the video capture
    data, image = capture.read()
    image = cv.cvtColor(cv.flip(image, 1), cv.COLOR_BGR2RGB)
    # Process the image and get the hand landmarks
    results = hands.process(image)
    # Convert the color space back from RGB to BGR for displaying with OpenCV
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    thumbsUp_detected = False
    fist_destected = False

    # If hand landmarks are detected, draw them on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections using MediaPipe's drawing utilities
            mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)
            if thumbsUp(hand_landmarks):
                thumbsUp_detected = True
            elif fist(hand_landmarks):
                fist_destected = True
    
    # If a thumbs up is detected, display the Payet image, or if is already open and is not detected close it
    if thumbsUp_detected:
        cv.imshow('Payet Thumbs Up', payet_img)
    else:
        if cv.getWindowProperty('Payet Thumbs Up', cv.WND_PROP_VISIBLE) >= 1:
            cv.destroyWindow('Payet Thumbs Up')
    
    if fist_destected:
        cv.imshow('Anderson Silva Fist', spider_fist)
    else:
        if cv.getWindowProperty('Anderson Silva Fist', cv.WND_PROP_VISIBLE) >= 1:
            cv.destroyWindow('Anderson Silva Fist')

    cv.imshow('Hand Tracking', image)   

    if cv.waitKey(20) & 0xFF==ord('d'):
        break


capture.release()
cv.destroyAllWindows()