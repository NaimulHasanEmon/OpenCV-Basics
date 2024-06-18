import cv2
img = cv2.imread('Computer Vision\img & vid\Lambo.png')
cv2.imshow('Image', img)
print(img.shape)

imgCropped = img[0:200, 200:500]
cv2.imshow('Cropped Image', imgCropped)
print(imgCropped.shape)

cv2.waitKey(0)
