
import cv2

pic = cv2.imread('PICT/photo_2023-07-28_00-55-48.jpg',0)

#resize image
#pic = cv2.resize(pic,(0,0), fx= 2, fy= 2)

#rotate image
#pic = cv2.rotate(pic, cv2.ROTATE_90_CLOCKWISE)

#save changes
cv2.imwrite('NEW.png',pic)

cv2.imshow('ED', pic)

#essential
cv2.waitKey(0)
cv2.destroyAllWindows()