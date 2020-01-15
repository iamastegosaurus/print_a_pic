import bpy
import csv

vertsData = []
w = 0
h = 0

with open('Q:\\print_a_pic\\rend2\\data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        a = float(row[0])
        b = float(row[1])
        c = 10 - float(row[2])
        vertsData.append([a, b, c])
        if a > w:
            w = a
        if b > h:
            h = b

w, h = int(w), int(h)
n = h*w

facesData = []

def get_faces():
    for yy in range( h-1 ):
        for xx in range( w-1 ):
            a = (xx) + (yy*w)
            b = (xx + 1) + (yy*w)
            c = (xx + 1) + ((yy+1) * w)
            d = (xx) + ((yy+1) * w)
            facesData.append( (a,b,c,d) )

get_faces()

mesh = bpy.data.meshes.new("myMesh_mesh")
mesh.from_pydata(vertsData, [], facesData) # verts, edges, faces
mesh.update()

new_object = bpy.data.objects.new("myMesh_object", mesh)
new_object.data = mesh
bpy.context.collection.objects.link(new_object)
