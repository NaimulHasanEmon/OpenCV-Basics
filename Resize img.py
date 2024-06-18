import cv2
img = cv2.imread('Computer Vision\img & vid\Lambo.png')
cv2.imshow('Image', img)
print(img.shape)

# Resize
imgResize = cv2.resize(img, (500, 350))
cv2.imshow('Resized Image', imgResize)

cv2.waitKey(0)
