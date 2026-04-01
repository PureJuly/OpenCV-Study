import cv2
import numpy as np

cap = cv2.VideoCapture(0)

lower_blue = np.array([100, 150, 50])
upper_blue = np.array([130, 255, 255])

ret, frame = cap.read()
canvas = np.zeros_like(frame)

prev_x, prev_y = 0, 0

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255),
          (0, 255, 255), (255, 0, 255), (255, 255, 0)]
color_idx = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    mask = cv2.erode(mask, None, iterations = 1)
    mask = cv2.dilate(mask, None, iterations = 3)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) > 0:
        c = max(contours, key = cv2.contourArea)
        M = cv2.moments(c)

        if M["m00"] > 0:
            center_x = int(M["m10"] / M["m00"])
            center_y = int(M["m01"] / M["m00"])

            if prev_x == 0 and prev_y == 0:
                prev_x, prev_y = center_x, center_y

            cv2.line(canvas, (prev_x, prev_y), (center_x, center_y), colors[color_idx], 5)

            prev_x, prev_y = center_x, center_y
    else:
        prev_x, prev_y = 0, 0

    result = cv2.add(frame, canvas)

    cv2.imshow("Air Canvas", result)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(10) & 0xFF

    if key == ord('c'):
        canvas = np.zeros_like(frame)
    elif key == ord('p'):
        color_idx = (color_idx + 1) % len(colors)
    elif key == 27:
        break

cap.release()
cv2.destroyAllWindows()
