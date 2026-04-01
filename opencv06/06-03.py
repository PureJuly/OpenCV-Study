import cv2

capture = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))

if capture.isOpened():
    print("카메라가 인식되었습니다.")

while True:
    ret, frame = capture.read()

    if not ret:
        break

    out.write(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(30) == 27:
        break

capture.release()
cv2.destroyAllWindows()