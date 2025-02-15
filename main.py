import cv2
import mediapipe as mp
import serial
import time

# Initialize serial communication with the Arduino
arduino = serial.Serial('COM4', 9600)  # Replace 'COM3' with your Arduino port
time.sleep(2)  # Wait for the connection to initialize

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Function to count the number of fingers up
def count_fingers(hand_landmarks):
    tips = [mp_hands.HandLandmark.THUMB_TIP,
            mp_hands.HandLandmark.INDEX_FINGER_TIP,
            mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            mp_hands.HandLandmark.RING_FINGER_TIP,
            mp_hands.HandLandmark.PINKY_TIP]

    pip_joints = [mp_hands.HandLandmark.INDEX_FINGER_PIP,
                  mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
                  mp_hands.HandLandmark.RING_FINGER_PIP,
                  mp_hands.HandLandmark.PINKY_PIP]

    landmarks = hand_landmarks.landmark
    finger_count = 0

    if landmarks[tips[0]].x < landmarks[mp_hands.HandLandmark.THUMB_IP].x:
        finger_count += 1

    for i in range(1, 5):
        if landmarks[tips[i]].y < landmarks[pip_joints[i-1]].y:
            finger_count += 1

    return finger_count

# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                                      mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                                      mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2))
            finger_count = count_fingers(hand_landmarks)
            cv2.putText(frame, str(finger_count), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Send the finger count to the Arduino
            arduino.write(f'{finger_count}'.encode())

    cv2.imshow('Hand Gesture Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
