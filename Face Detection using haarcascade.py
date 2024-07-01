import cv2

# Downloaded from opencv github
faceCascade = cv2.CascadeClassifier('Computer Vision\haarcascade_frontalface_default.xml')

img = cv2.imread('Computer Vision\img & vid\Lenna.png')
img =cv2.resize(img, (300, 300))
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(img, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow('Original Image', img)

cv2.waitKey(0)
