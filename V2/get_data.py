import cv2
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import math
import collections

import time
start = time.time()

img = cv2.imread('Q:\\print_a_pic\\images\\orange.jpg')
h, w, _ = img.shape

# PARAMS
hsv_bool = False
layers = 8
heightMod = 1.5
resize = False
max_px = 500000

if h * w > max_px:
    resize = True
    scale_percent = max_px / (h * w)

if resize == True:
 
    w_down = int(w * scale_percent)
    h_down = int(h * scale_percent)
    img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
    w, h = w_down, h_down
    print('new dim: ' + str(w) + ', ' + str(h))


if hsv_bool == True:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(img, 200, 200)
h, w, _ = img.shape

px_info = img.reshape(h*w, 3)

df = pd.DataFrame({
    'f1': px_info[0:, 0],
    'f2': px_info[0:, 1],
    'f3': px_info[0:, 2]
})

print("starting clust " + str(time.time() - start))

kmeans = KMeans(n_clusters = layers)
kmeans.fit(df)
z = kmeans.labels_

print("clust finished " + str(time.time() - start))

x, y = [], []
for j in range(h):
    for i in range(w):
        x.append(i)
        y.append(j)


def distances():
    meep = np.zeros(layers)
    count = np.zeros(layers)
    for t in range(layers):
        for p in range(h*w):
            if z[p] == t:
                meep[t] += math.sqrt( (w/2 - x[p])**2 + (h/2 - y[p])**2 )
                count[t] += 1
    return meep/count

d = {}
avg = distances()
for t in range(len(avg)):
    d[avg[t]] = t
od = collections.OrderedDict(sorted(d.items()))
reshape = list(od.values())[::-1]


def flipflop():
    for p in range(h*w):
        for t in range(len(reshape)):
            if z[p] == reshape[t]:
                z[p] = t
                break

flipflop()

print("flipflopped " + str(time.time() - start))

edgeValues = edge.reshape(h*w, 1)

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