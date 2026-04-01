import cv2

cats = cv2.imread(r"/pictures/catandcat.jpg")
cats = cv2.resize(cats, (512, 288))
woman = cv2.imread(r"/pictures/lena_copy.jpg")

green_mask = cv2.inRange(cats, (0, 120, 0), (100, 255, 100))
reverse_mask = cv2.bitwise_not(green_mask)

cats_merge = cv2.bitwise_and(cats, cats, mask = reverse_mask)
woman_merge = cv2.bitwise_and(woman, woman, mask = green_mask)

cats_woman = cv2.add(cats_merge, woman_merge)

cv2.imshow("Cats_woman", cats_woman)
cv2.waitKey()
cv2.destroyAllWindows()