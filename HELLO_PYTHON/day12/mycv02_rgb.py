import cv2
import matplotlib.pyplot as plt

img_color = cv2.imread('b.png', cv2.IMREAD_COLOR)
print(img_color)

cv2.imshow('color', img_color)

cv2.waitKey(0)

cv2.destroyAllWindows()

# red
# [[[ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]]
#
#  [[ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]]
#
#  [[ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]]
#
#  [[ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]
#   [ 36  28 237]]]

# green
# [[[ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]]
#
#  [[ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]]
#
#  [[ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]]
#
#  [[ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]
#   [ 76 177  34]]]

# blue
# [[[204  72  63]
#   [204  72  63]
#   [204  72  63]
#   [204  72  63]]
#
#  [[204  72  63]
#   [204  72  63]
#   [204  72  63]
#   [204  72  63]]
#
#  [[204  72  63]
#   [204  72  63]
#   [204  72  63]
#   [204  72  63]]
#
#  [[204  72  63]
#   [204  72  63]
#   [204  72  63]
#   [204  72  63]]]



# image = cv2.imread('dogs.jpg',1); 

# imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#
# height, width = 1980, 1520
#
# newsize = cv2.resize(imageRGB, (width, height))
#
# plt.subplot(1, 2, 1)
# plt.imshow(imageRGB)
#
# plt.subplot(1, 2, 2)
# plt.imshow(newsize)
#
# plt.show()