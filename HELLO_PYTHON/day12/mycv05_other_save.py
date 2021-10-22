import cv2

img_color = cv2.imread('dogs.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imwrite('dogs2.png',img_color,[cv2.IMWRITE_PNG_COMPRESSION])

cv2.imshow('color', img_color)

cv2.waitKey(0)

cv2.destroyAllWindows()

