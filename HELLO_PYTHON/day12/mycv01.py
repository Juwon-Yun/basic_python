import cv2
import matplotlib.pyplot as plt

img = cv2.imread('dogs.jpg', cv2.IMREAD_COLOR)
print(img)

cv2.imshow('color', img)

cv2.waitKey(0)

cv2.destroyAllWindows()

