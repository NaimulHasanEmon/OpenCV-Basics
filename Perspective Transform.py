import cv2
import numpy as np

img = cv2.imread('Computer Vision\img & vid\Cards.png')

width, height = 250, 350

pts1 = np.float32([[225,244], [408,209], [270, 515], [473,470]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('Original Image', img)
cv2.imshow('New Image', imgOutput)

cv2.waitKey(0)
