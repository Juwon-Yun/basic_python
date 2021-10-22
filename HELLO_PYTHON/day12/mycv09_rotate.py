import cv2

img_color = cv2.imread('dogs.jpg', cv2.IMREAD_COLOR)

height, width, channel = img_color.shape

matrix = cv2.getRotationMatrix2D((width/2, height/2),45,1)

dst = cv2.warpAffine(img_color, matrix, (width, height))

cv2.imshow('color', dst)

cv2.waitKey(0)

cv2.destroyAllWindows()

