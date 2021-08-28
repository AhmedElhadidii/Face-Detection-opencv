import cv2

# to load the date we are gonna use the
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#img = cv2.imread('profile pic.jpeg')
webcam = cv2.VideoCapture(0)

while True:
    frame_read, frame = webcam.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cords = trained_face_data.detectMultiScale(gray_img)
    print(face_cords)
    for (x, y, w, h) in face_cords:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('face detection app python', frame)
    cv2.waitKey(1)
# covert to gray
# show the face

   # detect faces


#show the output




print("CODE COMPLETED")
