import cv2
import numpy as np

img = cv2.imread('Computer Vision\img & vid\Lenna.png')
img = cv2.resize(img, (300, 300))

ver = np.vstack((img, img))

cv2.imshow('Vertical Stack Image', ver)

cv2.waitKey(0)
