import bpy
import csv

x = []
y = []
z = []

with open('Q:\\print_a_pic\\rend2\\data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

m = bpy.data.meshes.new( 'meshMoo' )

n = len(z)
m.vertices.add( n )
b = 0

for b in range(n):
    m.vertices[b].co = (x[b], y[b], z[b]) 

o = bpy.data.objects.new( 'objMoo', m )

bpy.context.collection.objects.link(o)

