import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img, "OpenCV", (300, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 200, 155), 2)
cv2.imshow('Image', img)

cv2.waitKey(0)
