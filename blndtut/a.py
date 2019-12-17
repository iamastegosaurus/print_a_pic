import bpy
import random

h = 30
w = 30

for x in range(w):
    for y in range(h):
        z = random.random() * 3
        bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x, y, z))
        print(x, y)

