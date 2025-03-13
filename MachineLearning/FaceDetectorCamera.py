import cv2
from random import randrange

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


webcam = cv2.VideoCapture(0)

while True:

    successful_frame_read, frame = webcam.read()
    if not successful_frame_read:
        break 


    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), 
                      (102, 255, 0), 2)
                     #(randrange(128, 256), randrange(128, 256), randrange(128, 256)), 2)

    cv2.imshow('Face Recogniser', frame)


    key = cv2.waitKey(1)
    if key == 27 or cv2.getWindowProperty('Face Recogniser', cv2.WND_PROP_VISIBLE) < 1:
        break


webcam.release()
cv2.destroyAllWindows()
print("Code Completed")
