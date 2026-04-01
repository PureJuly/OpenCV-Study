import cv2
import sys

img = cv2.imread(r'/pictures/lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]

img[10:100, 10:100] = [0, 0, 0]

cv2.imshow('Lena Window', img)

cv2.waitKey(0)
cv2.destroyAllWindows()