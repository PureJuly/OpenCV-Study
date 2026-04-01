import cv2
import numpy as np

src = cv2.imread(r"/pictures/coins.jpg")
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (11, 11), 0)
_, thresh = cv2.threshold(blur, 250, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(thresh, kernel, iterations = 1)

contours, hierarchy = \
cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

result = cv2.drawContours(src, contours, -1, (0, 255, 0), 2)

cv2.imshow('result', result)
cv2.imshow('dilation', dilation)
cv2.waitKey(0)
cv2.destroyAllWindows()