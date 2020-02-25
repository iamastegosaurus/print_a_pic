import bpy
import csv

vertsData = []
w = 0
h = 0

with open('Q:\\print_a_pic\\V2\\data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        a = float(row[0])
        b = float(row[1])
        c = float(row[2])
        vertsData.append([a, b, c])
        if a > w:
            w = a + 1
        if b > h:
            h = b + 1

w, h = int(w), int(h)
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


# bpy.ops.object.editmode_toggle()
# bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, -1.16415e-10, 10), "orient_type":'NORMAL', "orient_matrix":((0.688784, 0.724966, 0.000462525), (-0.724966, 0.688784, 7.90223e-05), (-0.000261292, -0.000389745, 1)), "orient_matrix_type":'NORMAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_target":'CLOSEST', "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "release_confirm":False, "use_accurate":False})
