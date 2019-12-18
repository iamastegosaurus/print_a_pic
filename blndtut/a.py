import bpy
import random
import math

h = 10
w = 10

for x in range(w):
    for y in range(h):
        z = math.sqrt(x*y)
        bpy.ops.surface.primitive_nurbs_surface_surface_add(radius=1, enter_editmode=False, location=(x, y, z))

