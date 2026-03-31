import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Python-OpenCV\tilted_book.png")

pts1 = np.float32([[101, 261], [271, 1258], [660, 97], [1160, 869]])
pts2 = np.float32([[0, 0], [0, 4000], [3000, 0], [3000, 4000]])

cv2.circle(img, (101, 261), 20, (255, 0, 0), -1)
cv2.circle(img, [271, 1258], 20, (0, 255, 0), -1)
cv2.circle(img, [660, 97], 20, (0, 0, 255), -1)
cv2.circle(img, (1160, 869), 20, (0, 0, 0), -1)

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img, M, (3000, 4000))

plt.subplot(121), plt.imshow(img), plt.title('Image')
plt.subplot(122), plt.imshow(dst), plt.title('Perspective')
plt.show()