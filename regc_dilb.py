import cv2
import threading
import face_recognition

# DEFINE CAMERA
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# SET CAMERA PROPORTION
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False

# LOAD REFERENCE IMAGE
ref_image = face_recognition.load_image_file('PICT/IMG-20230828-WA0044.jpg')
ref_encoding = face_recognition.face_encodings(ref_image)[0]

# VERIFY FACE VALIDITY
def check_face(frame):
    global face_match
    try:
        frame_encoding = face_recognition.face_encodings(frame)[0]
        results = face_recognition.compare_faces([ref_encoding], frame_encoding)
        face_match = results[0]
    except IndexError:
        face_match = False


while True:
    ret, frame = cam.read()

    if ret:
        if counter % 30 == 0:
            try:
                threading.Thread(target=check_face, args=(frame.copy(),)).start()

            except ValueError:
                pass
        counter += 1

        # DISPLAY MATCH
        if face_match:
            cv2.putText(frame, "MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "NO MATCH!", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow('frame', frame)

        # ESSENTIALS
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cv2.destroyAllWindows()
