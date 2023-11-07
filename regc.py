import cv2

import threading
from deepface import DeepFace

#DEFINE CAMERA
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#SET CAMERA PROPORTION
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 480)

counter = 0
face_match = False

#LOAD REFERENCE IMAGE
ref = cv2.imread('PICT/IMG-20230828-WA0044.jpg')

#VERIFY FACE VALIDITY
def check_face(frame):
    global face_match
    try:
        if DeepFace.verify(frame,ref.copy())['verified']:
            face_match = True

        else:
            face_match = False
    except ValueError:
        face_match = False


while True:
    ret, frame = cam.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face , args=(frame.copy(),).start())

            except ValueError:
                pass
                counter += 1



        #DISPLAY MATCH
        if face_match:
            cv2.putText(frame, "MATCH!" , (20,450), (0,255,0))

        else:
            cv2.putText(frame, "NO MATCH!" , (20,450), (0,0,255))

        cv2.imshow(frame)

        
#ESSENTIALS
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows