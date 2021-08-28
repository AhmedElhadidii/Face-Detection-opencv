import cv2
# to load the trained Data we are gonna use the
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#The Source
#img = cv2.imread('profile pic.jpeg')
webcam = cv2.VideoCapture(0)
#for the live feed of the webcam while loop is created
while True:
    frame_read, frame = webcam.read()
    #coverting to gray only because of the haarcascade algorithm
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #finding the face
    face_cords = trained_face_data.detectMultiScale(gray_img)
    #to print face cords on terminal
    print(face_cords)
    #loop to print rectangle on the facce on live
    for (x, y, w, h) in face_cords:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
#show output
    cv2.imshow('face detection app python', frame)
#refresh every 1 milisecond
    cv2.waitKey(101111)

    if key == 81 or key == 113:
        break


webcam.release()
print("CODE COMPLETED")
