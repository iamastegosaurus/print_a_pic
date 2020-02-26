import cv2
import pandas as pd
import numpy as np
import math
import os

img = cv2.imread('Q:\\print_a_pic\\images\\sunflower.jpg')
h, w, _ = img.shape
path = os.path.dirname(os.path.abspath(__file__))

# PARAMS
max_px = 300000

if h * w > max_px:

    scale_percent = max_px / (h * w)
    w_down = int(w * scale_percent)
    h_down = int(h * scale_percent)
    img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
    w, h = w_down, h_down
    # print('new dim: ' + str(w) + ', ' + str(h))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(w,h)
# cv2.imwrite('Q:\\print_a_pic\\color\\resized.jpg', img)
x, y, z = [], [], []

for j in range(h):
    for i in range(w):
        x.append(i)
        y.append(j)
        z.append( img[j, i]**0.25 )

save = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z
})

save.to_csv(path + '\\data.csv', index=False, header=False)

# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

os.system("blender --background --python " + path + "\\rend.py")