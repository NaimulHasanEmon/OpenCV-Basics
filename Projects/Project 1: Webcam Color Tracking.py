# This project uses OpenCV to detect and track multiple colors (white, yellow, red, green) in real-time video from a webcam. It identifies these colors using predefined HSV ranges, marks their positions with circles of corresponding colors on the screen, and updates their positions continuously as the objects move.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

frameWidth = 640
frameHeight = 480

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

def empty(a):
    pass

myColors = [[110, 26, 149, 161, 255, 255],       # White
            [15, 40, 130, 35, 255, 255],         # Yellow
            [170, 50, 120, 180, 255, 255],       # Red
            [63, 49, 92, 91, 255, 255]]          # Green

# Color values must be in BGR format
myColorValues = [[255, 255, 255],
                [141, 255, 255],
                [80, 83, 239],
                [83, 200, 0]]

myPoints = []           # [x, y, colorId]

def findColors(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 7, myColorValues[count], cv2.FILLED)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(f'Masked {color}', mask)
    return newPoints

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0         # for the case in which the loop may not get any values
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 100:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 7, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColors(imgResult, myColors, myColorValues)

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValues)

    cv2.imshow('Video', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
