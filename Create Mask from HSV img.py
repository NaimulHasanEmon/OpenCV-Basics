import cv2
import numpy as np

def empty(a):
    pass

cv2.namedWindow('TrackBars')
cv2.resizeWindow('TrackBars', 640, 240)
cv2.createTrackbar('Hue Min', 'TrackBars', 0, 179, empty)
cv2.createTrackbar('Hue Max', 'TrackBars', 22, 179, empty)
cv2.createTrackbar('Sat Min', 'TrackBars', 69, 255, empty)
cv2.createTrackbar('Sat Max', 'TrackBars', 255, 255, empty)
cv2.createTrackbar('Val Min', 'TrackBars', 35, 255, empty)
cv2.createTrackbar('Val Max', 'TrackBars', 255, 255, empty)

while True:
    img = cv2.imread('Computer Vision\img & vid\Lambo.png')
    img = cv2.resize(img, (403, 300))       # Resize the original image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min', 'TrackBars')
    h_max = cv2.getTrackbarPos('Hue Max', 'TrackBars')
    s_min = cv2.getTrackbarPos('Sat Min', 'TrackBars')
    s_max = cv2.getTrackbarPos('Sat Max', 'TrackBars')
    v_min = cv2.getTrackbarPos('Val Min', 'TrackBars')
    v_max = cv2.getTrackbarPos('Val Max', 'TrackBars')
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)

    cv2.imshow('Original Image', img)
    cv2.imshow('HSV Image', imgHSV)
    cv2.imshow('Mask Image', mask)

    cv2.waitKey(1)
