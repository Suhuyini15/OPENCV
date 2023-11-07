import cv2
import pathlib

# Get the path to the Haar cascade file

cascade_path = pathlib.Path(cv2.__file__).parent / r"C:\Users\DELL\anaconda3\pkgs\opencv-4.6.0-py39hf11a4ad_3\Library\etc\haarcascades\haarcascade_frontalface_default.xml"

#print(cascade_path)
clf = cv2.CascadeClassifier(str(cascade_path))

camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = clf.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

    cv2.imshow("Faces", frame)
    if cv2.waitKey(1) == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
