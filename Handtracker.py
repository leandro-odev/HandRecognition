# Library: OpenCV, Mediapipe
import cv2 as cv
import mediapipe as mp

# Initialize MediaPipe drawing utilities and hand tracking module
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mphands = mp.solutions.hands

# Start capturing video from the default camera (example: on a laptop is the webcam. if 0 is not working, try 1 and so on, because it depends on the number of cameras connected to the device)
capture = cv.VideoCapture(0)
# Initialize the MediaPipe Hands solution
hands = mphands.Hands()

while True:
    # Read a frame from the video capture
    data, image = capture.read()
    # Flip the image horizontally for a later selfie-view display
    image = cv.cvtColor(cv.flip(image, 1), cv.COLOR_BGR2RGB)
    # Process the image and get the hand landmarks
    results = hands.process(image)
    # Convert the color space back from RGB to BGR for displaying with OpenCV
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)

    # If hand landmarks are detected, draw them on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections using MediaPipe's drawing utilities
            mp_drawing.draw_landmarks(image, hand_landmarks, mphands.HAND_CONNECTIONS)

    # Display the resulting frame with hand landmarks
    cv.imshow('Hand Tracking', image)

    # Wait for 20 milliseconds and check if the 'd' key has been pressed to break the loop
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

# Release the video capture object and close all OpenCV windows
capture.release()
cv.destroyAllWindows()