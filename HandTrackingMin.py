import cv2
import mediapipe as mp
import time

ptime = 0
ctime = 0
cap = cv2.VideoCapture(0)

mphand = mp.solutions.hands
mpdraw = mp.solutions.drawing_utils
hand = mphand.Hands()

while True:
    success, img = cap.read()
    imgr = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # detection
    result = hand.process(imgr)
    #     print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handlms in result.multi_hand_landmarks:
            for id, lm in enumerate(handlms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
            mpdraw.draw_landmarks(img, handlms, mphand.HAND_CONNECTIONS)

    ctime = time.time()
    fps = 1 / (ctime - ptime)
    ptime = ctime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("detection", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
