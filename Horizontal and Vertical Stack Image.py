import cv2
import numpy as np

img = cv2.imread('Computer Vision\img & vid\Lenna.png')
img = cv2.resize(img, (200, 200))

hor = np.hstack((img, img))    # Horizontal
ver = np.vstack((img, img))    # Vertical

cv2.imshow('Horizontal Image', hor)
cv2.imshow('Vertical Image', ver)

cv2.waitKey(0)
