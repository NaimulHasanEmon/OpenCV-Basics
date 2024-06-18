import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
print(img)
img[:] = 255,0,0             # Code is for blue color
cv2.imshow('Image', img)

cv2.waitKey(0)
