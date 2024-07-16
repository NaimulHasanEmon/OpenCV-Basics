import cv2

cap = cv2.VideoCapture('Computer Vision\Videos\Car License Plate\sample9.webm')

frameWidth = 640
frameHeight = 480

cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

numberPlateCascade = cv2.CascadeClassifier('Computer Vision\haarcascades\haarcascade_russian_plate_number.xml')
minArea = 500
color = (0, 0, 0)
count = 0

while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))

    numberPlates = numberPlateCascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, 'Number Plate', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 1, color, 2)
            imgRoi = img[y:y+h, x:x+w]
            cv2.imshow('ROI', imgRoi)

    cv2.imshow('Result', img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.imwrite('Computer Vision\\Scanned\\NoPlate_'+str(count)+'.jpg', imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, 'Scan saved', (150, 260), cv2.FONT_HERSHEY_COMPLEX, 2, color, 2)
        cv2.imshow('Result', img)
        cv2.waitKey(500)
        count += 1
