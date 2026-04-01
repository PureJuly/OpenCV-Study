import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

tiger = cv2.imread(r"C:\Python-OpenCV\tigermask.png", cv2.IMREAD_UNCHANGED)
orig_h, orig_w = tiger.shape[:2]

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 5)

    for (x, y, w, h) in faces:
        scale = 2

        new_w = int(w * scale)
        new_h = int(new_w * (orig_h / orig_w))
        new_x = x - int((new_w - w) / 2)
        new_y = y - int((new_h - h) / 2)

        if new_x < 0 or new_y < 0 or new_x + new_w > frame.shape[1] or new_y + new_h > frame.shape[0]:
            continue

        tiger_resize = cv2.resize(tiger, (new_w, new_h))

        img_bgr = tiger_resize[:, :, 0:3]
        img_alpha = tiger_resize[:, :, 3]

        _, mask = cv2.threshold(img_alpha, 1, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        roi = frame[new_y : new_y + new_h, new_x : new_x + new_w]
        roi_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
        roi_fg = cv2.bitwise_and(img_bgr, img_bgr, mask = mask)

        dst = cv2.add(roi_bg, roi_fg)
        frame[new_y : new_y + new_h, new_x : new_x + new_w] = dst

        print(f"위치값: {new_x}, {new_y}, {new_w}, {new_h}")

    cv2.imshow("frame", frame)

    if cv2.waitKey(10) == ord('q'):  # ESC 키
        break

cap.release()
cv2.destroyAllWindows()