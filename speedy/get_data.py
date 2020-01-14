import pandas as pd
import cv2
import numpy as np
from sklearn.cluster import KMeans
import math
import collections

import time
start = time.time()

img = cv2.imread('Q:\\print_a_pic\\images\\sunflower.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
edge = cv2.Canny(img, 200, 200)
h, w, _ = img.shape

# PARAMS
layers = 7
heightMod = 1.2
resize = False
scale_percent = .5

bgrpx = img.reshape(h*w, 3)
hsvpx = hsv.reshape(h*w, 3)

df = pd.DataFrame({
    'f1': bgrpx[0:, 0],
    'f2': bgrpx[0:, 1],
    'f3': bgrpx[0:, 2]
})

print("imports and data loaded " + str(time.time() - start))

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

print("starting flipflop " + str(time.time() - start))

flipflop()

print("flipflop complete " + str(time.time() - start))

edgeValues = edge.reshape(h*w, 1)

def add_edges():
    for t in range(len(z)):
        if edgeValues[t] == 255:
            z[t] += .5

            # if z[t] <= layers / 2:
            #     z[t] = layers
            # else:
            #     z[t] = 0

add_edges()
for pt in range(len(z)):
    # z[pt] = z[pt] * 255 / layers # TO DISPLAY
    z[pt] = z[pt] * heightMod # * 255 / layers # SCALE DOWN FOR RENDER

print("edges added " + str(time.time() - start))

new = gray.copy()
p = 0
for j in range(h):
    for i in range(w):
        new[j][i] = z[p]
        p += 1

kernel = np.ones((5, 5), np.float32) / 25
blur = cv2.filter2D(new, -1, kernel)

# cv2.imwrite(''Q:\\print_a_pic\\rend\\img.jpg', new)

print("blurred and finished. total time: " + str(time.time() - start))


if resize == True:
 
    w_down = int(w * scale_percent)
    h_down = int(h * scale_percent)
    down = cv2.resize(blur, (w_down, h_down), interpolation = cv2.INTER_AREA)

# cv2.imshow('new', new)
# cv2.imshow('blur', blur)
# cv2.imshow('down', down)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# USE TO SAVE
x = []
y = []
z = []

for i in range(w):
    for j in range(h):
        x.append(i)
        y.append(j)
        z.append(blur[j, i])

save = pd.DataFrame({
    'x': x,
    'y': y,
    'z': z
})

save.to_csv('Q:\\print_a_pic\\rend2\\data.csv', index=False, header=False)