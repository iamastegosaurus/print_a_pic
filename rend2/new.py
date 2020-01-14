import bpy
import csv

vertsData = []

with open('Q:\\print_a_pic\\rend2\\data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
        vertsData.append([a, b, c])

w = 400
h = 400
n = h*w
facesData = []

def get_faces():
    for yy in range( h-1 ):
        for xx in range( w-1 ):
            a = (xx) + (yy*h)
            b = (xx + 1) + (yy*h)
            c = (xx + 1) + ((yy+1) * h)
            d = (xx) + ((yy+1) * h)
            facesData.append( (a,b,c,d) )

get_faces()
# vertsData =[(1,-1,-1),(1,-1,1),(-1,-1,1),(-1,-1,-1),(1,1,-1),(1,1,1),(-1,1,1),(-1,1,-1)]
# facesData = [ (0, 399, 159400, 159201) ]# [(0,1,2,3),(4,7,6,5),(1,5,6,2),(2,6,7,3),(4,0,3,7)]

mesh = bpy.data.meshes.new("myMesh_mesh")
mesh.from_pydata(vertsData, [], facesData) # verts, edges, faces
mesh.update()

new_object = bpy.data.objects.new("myMesh_object", mesh)
new_object.data = mesh
bpy.context.collection.objects.link(new_object)
