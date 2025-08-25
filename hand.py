import cv2
import mediapipe as mp
import math
import time

# Initialize MediaPipe hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

bullet_list = []
bullet_speed = 20

def is_shooting_gesture(landmarks):
    """Detect if only index finger is up (shoot gesture)."""
    # Tip IDs for fingers
    tip_ids = [4, 8, 12, 16, 20]

    fingers = []
    # Thumb
    fingers.append(landmarks[tip_ids[0]].x < landmarks[tip_ids[0]-1].x)

    # Other fingers
    for i in range(1, 5):
        fingers.append(landmarks[tip_ids[i]].y < landmarks[tip_ids[i]-2].y)

    # Shooting gesture: index up, others down
    return fingers[1] and not any(fingers[2:])

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    h, w, _ = img.shape

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            if is_shooting_gesture(hand_landmarks.landmark):
                # Get fingertip position (index finger tip = id 8)
                x = int(hand_landmarks.landmark[8].x * w)
                y = int(hand_landmarks.landmark[8].y * h)
                bullet_list.append([x, y, time.time()])

    # Move bullets
    for bullet in bullet_list[:]:
        bullet[1] -= bullet_speed
        cv2.circle(img, (bullet[0], bullet[1]), 8, (0, 0, 255), -1)
        if bullet[1] < 0:
            bullet_list.remove(bullet)

    cv2.imshow("Hand Shooting Game", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
