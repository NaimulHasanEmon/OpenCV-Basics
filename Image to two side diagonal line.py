import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0,0),(img.shape[1], img.shape[0]),(0, 0, 255), 3)
cv2.line(img, (0, img.shape[1]),(img.shape[0], 0),(0, 0, 255), 3)
cv2.imshow('Image', img)

cv2.waitKey(0)
