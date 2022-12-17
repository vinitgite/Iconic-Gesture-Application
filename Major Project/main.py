import os
import cv2
import shutil
import numpy as np
from cvzone.HandTrackingModule import HandDetector

# variables
width, height = 1550, 778
folderPath = "imag"
x = 0

# Camera Setup
cap = cv2.VideoCapture(0)
cap.set(3, width)
cap.set(4, height)

# get the list of presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
# print(pathImages)

# Variables
imgNumber = 0
hs, ws = int(120 * 1.2), int(213 * 1.2)
gestureThreshold = 280
buttonPress = False
buttonCounter = 0
buttonDelay = 20
annotations = [[]]
annotationNumber = 0
annotationStart = False

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Import images
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 8)
    #print(annotationNumber)

    if hands and buttonPress is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        cx, cy = hand['center']
        lmList = hand['lmList']

        # Constrain the values for easier drawing
        assert isinstance(w, object)
        xVal = int(np.interp(lmList[8][0], [width // 2, w], [0, width]))
        yVal = int(np.interp(lmList[8][1], [180, height - 175], [0, height]))
        indexFinger = xVal, yVal
        # print(fingers)

        if cy <= gestureThreshold:  # if hand is at the height of face
            annotationStart = False
            # Gesture 1 - Left
            if fingers == [1, 0, 0, 0, 0]:
                annotationStart = False
                # print("Left")
                if imgNumber > 0:
                    buttonPress = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber -= 1

            # Gesture 2 - Right
            if fingers == [0, 0, 0, 0, 1]:
                annotationStart = False
                # print("Right")
                if imgNumber < len(pathImages) - 1:
                    buttonPress = True
                    annotations = [[]]
                    annotationNumber = 0
                    imgNumber += 1

            # Gesture 3 - Going to first slide
            if fingers == [1, 1, 0, 0, 0]:
                annotationStart = False
                buttonPress = True
                annotations=[[]]
                annotationNumber=0                
                imgNumber = 0

            #  Gesture 4 - Going to last slide 
            if fingers == [1, 0, 0, 0, 1]:
                annotationStart = False
                buttonPress = True
                annotations=[[]]
                annotationNumber=0                
                imgNumber = len(pathImages) - 1

        # Gesture 5 - Showing Pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 8, (0, 0, 255), cv2.FILLED)
            annotationStart = False
        # Gesture 6 - Drawing mode
        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 12, (0, 0, 255), cv2.FILLED)
            annotations[annotationNumber].append(indexFinger)
        else:
            annotationStart = False
    
        # Gesture 7 - Erase
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                if annotationNumber >= 0:
                    annotations.pop(-1)
                    annotationNumber -= 1
                    buttonPress = True
    else:
        annotationStart = False
    # Button Pressed Iterations
    if buttonPress:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPress = False

    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0, 0, 200), 5)

    # Adding webcam image on the slides
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall

    # cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == 27: 
        os.remove("sample.pdf")
        shutil.rmtree("imag",ignore_errors=False)
        cv2.destroyAllWindows()
        break

