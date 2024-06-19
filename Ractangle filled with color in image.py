import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
cv2.rectangle(img, (100, 100), (200, 200), (255, 0, 0), cv2.FILLED)
cv2.imshow('Image', img)

cv2.waitKey(0)
