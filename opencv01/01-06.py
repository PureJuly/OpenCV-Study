import cv2
import sys

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("왼쪽 버튼 클릭:", x, y)
    elif event == cv2.EVENT_RBUTTONDBLCLK:
        print("오른쪽 버튼 더블 클릭:", x, y)

img = cv2.imread(r'C:\Python-OpenCV\lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

cv2.imshow('Lena Window', img)
cv2.setMouseCallback('Lena Window', mouse_callback)

cv2.waitKey(0)
cv2.destroyAllWindows()