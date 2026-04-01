import cv2

img = cv2.imread(r'/pictures/lena.jpg')
dst1 = cv2.resize(img, None, fx = 0.5, fy = 0.5,interpolation = cv2.INTER_LINEAR)
dst2 = cv2.resize(img, None, fx = 0.75, fy = 0.75, interpolation = cv2.INTER_CUBIC)
dst3 = cv2.resize(img, None, fx = 1.25, fy = 1.25, interpolation = cv2.INTER_AREA)

cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()
