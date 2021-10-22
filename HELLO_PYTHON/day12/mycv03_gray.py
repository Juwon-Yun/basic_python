import cv2

img_color = cv2.imread('dogs.jpg', cv2.IMREAD_GRAYSCALE)
print(img_color)

cv2.imshow('color', img_color)

cv2.waitKey(0)

cv2.destroyAllWindows()

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