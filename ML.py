import cv2 as cv

camera = 0  #change camera here
capture = cv.VideoCapture(camera) #captures video

while True:
    isTrue,frame = capture.read() #Read and stores the frames in frame variable

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #changes image color to gray

    haar_cascade = cv.CascadeClassifier('haarcascade_profileface.xml') #change haarcascade file here

    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) #detects face

    for (x, y, w, h) in faces_rect:  # draws rectange around the face
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2) #change color & thickness of rectangle here

    cv.imshow('video', frame) #display window

    if cv.waitKey(20) & 0xFF==ord('d'): #window closes if you press 'd'
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
