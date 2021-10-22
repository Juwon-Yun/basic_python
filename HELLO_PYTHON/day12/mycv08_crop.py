import cv2

img_color = cv2.imread('dogs.jpg', cv2.IMREAD_COLOR)

y = 0
h = 500
x = 0
w = 500

cropped_img = img_color[y:y + h, x: x + w]

cv2.imshow('color', cropped_img)

cv2.waitKey(0)

cv2.destroyAllWindows()

