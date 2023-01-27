import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
# https://github.com/opencv/opencv/tree/master/data/haarcascades
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier("eye.xml")
# 0 is camera index. Refers to default camera means webcam
cap = cv2.VideoCapture(0)

blinkCount = 0
eyeClose = False

while True:
    ret, img = cap.read()  # ret is boolean value. It return true if frame is available
    grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    if not ret:
        break
    # detectMultiScale openCV function is used to detect the faces
    faces = face_cascade.detectMultiScale(grayImage)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (80, 77, 250), 2)
        cv2.putText(img, "face", (x, y - 4), 1, 1, (255, 0, 0))
        face = img[y : y + h, x : x + w]
        grayFace = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(grayFace, 1.3)
        if len(eyes) == 0:  # No eyes in image or eyes or closed
            if not eyeClose:
                blinkCount += 1
                eyeClose = True
        else:
            eyeClose = False
        cv2.putText(img, "Blinks: " + str(blinkCount), (5, 25), 1, 2, (0, 155, 0),2)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(face, (ex, ey), (ex + ew, ey + eh), (0, 255, 0))
            cv2.putText(face, "eye", (ex, ey - 4), 1, 1, (255, 0, 0))

    cv2.imshow("Face Detection", img)
    cv2.waitKey(10)
cap.release()
cv2.destroyAllWindows()
