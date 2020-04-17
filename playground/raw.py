import numpy as np
from stl import mesh
import os
import cv2
import time

path = os.path.dirname(os.path.abspath(__file__))

# vertices = np.array([
#     [-1, -1, -1],
#     [+1, -1, -1],
#     [+1, +1, -1],
#     [-1, +1, -1],
#     [-1, -1, +1],
#     [+1, -1, +1],
#     [+1, +1, +1],
#     [-1, +1, +1]])
# faces = np.array([
#     [0,3,1],
#     [1,3,2],
#     [0,4,7],
#     [0,7,3],
#     [4,5,6],
#     [4,6,7],
#     [5,1,2],
#     [5,2,6],
#     [2,3,6],
#     [3,7,6],
#     [0,1,5],
#     [0,5,4]])
max_kpx = 200000

t = time.time()

img = cv2.imread(path + "\\images\\" + 'sunflower.jpg')
h, w, _ = img.shape
max_px = max_kpx * 1000

if h * w > max_px:

    scale_percent = max_px / (h * w)
    w_down = int(w * math.sqrt(scale_percent))
    h_down = int(h * math.sqrt(scale_percent))
    img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
    w, h = w_down, h_down

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

vertices = []
faces = []

print(time.time() - t)
t = time.time()

for j in range(h):
    for i in range(w):
        vertices.append([i - w/2, j - h/2, img[j,i] ]) 

print(time.time() - t)
t = time.time()

def get_faces():
    for yy in range( h-1 ):
        for xx in range( w-1 ):
            a = (xx) + (yy*w)
            b = (xx + 1) + (yy*w)
            c = (xx + 1) + ((yy+1) * w)

            faces.append( (a,b,c) )

            b = (xx + 1) + (yy*w)
            c = (xx + 1) + ((yy+1) * w)
            d = (xx) + ((yy+1) * w)

            faces.append( (b,c,d) )

get_faces()

print(time.time() - t)
t = time.time()

depth = -12
vertices.append( [0, 0, depth] )
vertices.append( [w, 0, depth] )
vertices.append( [0, h, depth] )
vertices.append( [w, h, depth] )

faces.append( [w*h + 1, w*h + 2, w*h + 3] )
faces.append( [w*h + 2, w*h + 3, w*h + 4] )


faces = np.array(faces)
vertices = np.array(vertices)

mash = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))

print(time.time() - t)
t = time.time()

for i, f in enumerate(faces):
    for j in range(3):
        mash.vectors[i][j] = vertices[f[j],:]

print(time.time() - t)
t = time.time()

mash.save(path + '\\test.stl')