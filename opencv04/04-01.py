import cv2
import numpy as np

img = cv2.imread(r'C:\Python-OpenCV\lena.jpg', cv2.IMREAD_GRAYSCALE)

# dx=1, dy=0: 수직 에지 검출
sobel_x = cv2.Sobel(img, -1, 1, 0, ksize=3)

# dx=0, dy=1: 수평 에지 검출
sobel_y = cv2.Sobel(img, -1, 0, 1, ksize=3)

dst = cv2.add(sobel_x, sobel_y)

cv2.imshow('Sobel X', sobel_x)
cv2.imshow('Sobel Y', sobel_y)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()