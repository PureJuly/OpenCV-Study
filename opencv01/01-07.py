## 실습 과제 : 나만의 그림판 만들기

### 마우스를 이용하여 빈 캔버스에 자유롭게 그림을 그리는 프로그램을 작성하세요.

# 1. `512x512` 크기의 흰색 빈 이미지를 생성합니다.
# 2. 마우스 **왼쪽 버튼을 누른 채로 이동(Drag)** 하면 검은색(`(0, 0, 0)`) 선이 그려져야 합니다.
# 3. 마우스 버튼을 놓으면 그리기가 멈춰야 합니다.
# 4. 키보드 `c`를 누르면 캔버스가 초기화(Clear) 됩니다.
# 5. 키보드 `q` 또는 `ESC`를 누르면 프로그램이 종료됩니다.

import cv2
import numpy as np

canvas = np.full((512, 512, 3), 255, dtype=np.uint8)


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        if flags == cv2.EVENT_FLAG_LBUTTON:
            cv2.circle(canvas, (x, y), 3, (0, 0, 0), -1)


while True:
    cv2.imshow('Canvas', canvas)
    cv2.setMouseCallback('Canvas', mouse_callback)
    key = cv2.waitKey(10)
    if key == ord('c'):
        canvas = np.full((512, 512, 3), 255, dtype=np.uint8)
    elif key == ord('q') or key == 27:
        break

cv2.destroyAllWindows()