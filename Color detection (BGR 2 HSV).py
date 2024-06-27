import cv2
import numpy as np

img = cv2.imread('Computer Vision\img & vid\Lambo.png')
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('Original Image', img)
cv2.imshow('HSV Image', imgHSV)

cv2.waitKey(0)
