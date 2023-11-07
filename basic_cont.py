import cv2
import random

pic = cv2.imread('PICT/photo_2023-07-28_01-31-06.jpg')
pic = cv2.resize(pic, (0,0), fx= 0.5, fy= 0.5)

#print array
print(pic[500])

#change picture
for i in range(200):
    for j in range(pic.shape[1]):
        pic[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]


cv2.imshow('ED2', pic)

#essentials
cv2.waitKey(0)
cv2.destroyAllWindows()