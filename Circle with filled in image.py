import cv2
import numpy as np

img = np.zeros((312, 312, 3), np.uint8)
cv2.circle(img, (int(img.shape[1]/2), int(img.shape[0]/2)), 30, (0, 0, 255), cv2.FILLED)
cv2.imshow('Image', img)

cv2.waitKey(0)
