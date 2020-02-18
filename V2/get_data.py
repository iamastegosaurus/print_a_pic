import cv2

import pandas as pd
import numpy as np
import math
import collections


img = cv2.imread('Q:\\print_a_pic\\images\\orange.jpg')
h, w, _ = img.shape

# PARAMS
max_px = 500000

if h * w > max_px:

    scale_percent = max_px / (h * w)
    w_down = int(w * scale_percent)
    h_down = int(h * scale_percent)
    img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
    w, h = w_down, h_down
    # print('new dim: ' + str(w) + ', ' + str(h))



img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)




x, y = [], []
for j in range(h):
    for i in range(w):
        x.append(i)
        y.append(j)




def add_edges():
    for t in range(len(z)):
        if edgeValues[t] == 255:
            z[t] += 10

add_edges()
for pt in range(len(z)):
    # z[pt] = z[pt] * 255 / layers # TO DISPLAY
    z[pt] = z[pt] * heightMod

new = gray.copy()
p = 0
for j in range(h):
    for i in range(w):
        new[j][i] = z[p]
        p += 1

kernel = np.ones((5, 5), np.float32) / 25
blur = cv2.filter2D(new, -1, kernel)

print("edges and blur. total time:  " + str(time.time() - start))

x = []
y = []
z = []

for j in range(h):
    for i in range(w):
        x.append(i)
        y.append(j)
        z.append(blur[j, i])

save = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z
})

save.to_csv('Q:\\print_a_pic\\V2\\data.csv', index=False, header=False)

cv2.imshow('new', new)
cv2.imshow('blur', blur)
cv2.waitKey(0)
cv2.destroyAllWindows()