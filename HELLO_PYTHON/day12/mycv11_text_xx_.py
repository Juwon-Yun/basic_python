import cv2

import numpy as np

from PIL import ImageFont, ImageDraw, Image

print(np.__version__)

print(Image.__version__)

print(cv2.__version__)

# 1.19.5

# 8.2.0

# 4.5.3

filepath = "image/pengsu.png"

original = cv2.imread(filepath, cv2.IMREAD_COLOR)

b, g, r, a = 255, 255, 255, 0

fontpath = "fonts/4.ttc"

# fontpath = "fonts/gulim.ttc"

# fontpath = "HMKMRHD.TTF"

font = ImageFont.truetype(fontpath, 20)

img_pil = Image.fromarray(original)

draw = ImageDraw.Draw(img_pil)

draw.text((60, 70), "김형준ABC123#GISDeveloper", font=font, fill=(b, g, r, a))

original = np.array(img_pil)

cv2.imshow('Original', original)

cv2.waitKey(0)

cv2.destroyAllWindows()
