import cv2
img = cv2.imread('Computer Vision\img & vid\Wallpaper3.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray image', imgGray)
cv2.waitKey(0)
