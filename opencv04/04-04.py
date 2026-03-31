# 허프 원 검출
import cv2
import numpy as np

src = cv2.imread('C:\Python-OpenCV\shape.png')
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
circles1 = cv2.HoughCircles(gray, dp=1, minDist=50, param2=15)

circles1 =  np.int32(circles1)
print('circles1.shape=', circles1.shape)
for circle in circles1[0,:]:
    cx, cy, r  = circle
    cv2.circle(src, (cx, cy), r, (0,0,255), 2)
cv2.imshow('src',  src)

cv2.waitKey()
cv2.destroyAllWindows()