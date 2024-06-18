import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

# Original image
img = cv2.imread('Computer Vision\img & vid\Lenna.png')

# Canny image from original image
imgCanny = cv2.Canny(img, 100, 100)
cv2.imshow('Canny Image from original', imgCanny)

# Dilate image from canny image
imgDilate = cv2.dilate(imgCanny, kernel, iterations = 1)
cv2.imshow('Dilate Image from canny', imgDilate)

cv2.waitKey(0)
