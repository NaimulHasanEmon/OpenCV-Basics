import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.line(img, (0,0), (300, 300), (0,255,0), 3)
cv2.imshow('Line in image', img)

cv2.waitKey(0)
