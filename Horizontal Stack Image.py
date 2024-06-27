import cv2
import numpy as np

img = cv2.imread('Computer Vision\img & vid\Lenna.png')
img = cv2.resize(img, (300, 300))

hor = np.hstack((img, img))

cv2.imshow('Horizontal Stack Image', hor)

cv2.waitKey(0)
