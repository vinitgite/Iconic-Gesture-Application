import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

# Variables
width , height = 600, 320 
gestureThreshold = 150

# Camera Setup

cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# Hand Detector
detector = HandDetector(detectionCon=0.5, maxHands=1)
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1) # Here 1 means horizontal and 0 means vertical
    hands, img = detector.findHands(img)
    cv2.line(img,(0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 3) # Threshold line

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        # print(fingers)

        if cy <= gestureThreshold:  #If hand is at the height of the face
            
            # Gestures
            if fingers == [1, 1, 1, 1, 1]:
                time.sleep(1.2)
                pyautogui.press("space", presses=1)
                # time.sleep(1)
            # elif fingers == [0, 1, 1, 1, 0]:
            #     pyautogui.press('pause', presses=2)
            elif fingers == [1, 0, 0, 0, 0]:
                pyautogui.press('prevtrack', presses=1)
                time.sleep(0.5)
                pyautogui.press('left', presses=1)
            elif fingers == [0, 0, 0, 0, 1]:
                pyautogui.press('nexttrack', presses=1)
                time.sleep(0.5)
                pyautogui.press('right', presses=1)
            elif fingers == [0, 1, 0, 0, 0]:
                pyautogui.press('volumeup', presses=1)
            elif fingers == [0, 1, 1, 0, 0]:
                pyautogui.press('volumedown', presses=1)
            elif fingers == [0, 1, 1, 1, 0]:
                time.sleep(0.8)
                pyautogui.press('volumemute', presses=1)
            # Full screen
            # elif fingers == [1, 0, 0, 0, 1]:
            #     time.sleep(0.5)
            #     pyautogui.press('f')


    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyAllWindows()
        break     