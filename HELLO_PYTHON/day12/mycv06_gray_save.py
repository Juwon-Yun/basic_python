import cv2

img_color = cv2.imread('dogs.jpg', cv2.IMREAD_COLOR)

dst2 = cv2.resize(img_color, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
cv2.imshow('color', dst2)

cv2.waitKey(0)

cv2.destroyAllWindows()

