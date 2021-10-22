import cv2
import imutils

img_color = cv2.imread('dogs.jpg', cv2.IMREAD_COLOR)

dst = imutils.translate(img_color, 25, -75)

dst = imutils.rotate(img_color, angle=45, center=(0,0))

dst = imutils.auto_canny(img_color)

cv2.imshow('color', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()

