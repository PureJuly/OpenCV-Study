import cv2

img = cv2.imread(r'C:\Python-OpenCV\lena.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = gray[250:290, 250:350]

res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

top_left = max_loc
gray = cv2.circle(gray, top_left, 5, (0, 0, 0), -1)

cv2.imshow('gray', gray)
cv2.imshow('template', template)
cv2.waitKey(0)
cv2.destroyAllWindows()