import cv2
import numpy as np
import dlib

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open the webcam")

detector = dlib.get_frontal_face_detector()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = detector(gray)
    i = 0

    for face in faces:
        x, y = face.left(), face.top()
        x1, y1 = face.right(), face.bottom()
        cv2.rectangle(frame, (x, y), (x1, y1), (0,255, 0), 2)
        i+=1
        cv2.putText(frame,'face num'+str(i),(x-10, y-10),cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 0, 255), 2)
        print(face, i)

    cv2.putText(frame, f'Number of faces: {i}', (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    cv2.imshow("Video",frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        

cap.release()
cv2.destroyAllWindows()