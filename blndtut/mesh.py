import bpy
import random

m = bpy.data.meshes.new( 'meshMoo' )
side = 1000

n = side**2
m.vertices.add( n )
b = 0

for i in range(side):
    for j in range(side):
        k = random.randint(0, 10)
        m.vertices[b].co = (i, j, k) 
        b += 1

o = bpy.data.objects.new( 'objMoo', m )

bpy.context.collection.objects.link(o)
