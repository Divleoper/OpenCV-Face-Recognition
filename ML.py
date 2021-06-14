import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    haar_cascade = cv.CascadeClassifier('haarcascade_profileface.xml')

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    cv.imshow('video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

#image = cv.resize(img, (1240, 880))
#cv.imshow("detected face", img)


cv.waitKey(0)
