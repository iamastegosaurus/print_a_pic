import bpy
import csv
import os

vertsData = []
w = 0
h = 0
path = os.path.dirname(os.path.abspath(__file__))

with open(path + '\\data.csv') as csvfile:
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
# print(w,h)
for pt in range(len(vertsData)):
    # print(vertsData[pt])
    vertsData[pt][0] -= int(w/2)
    vertsData[pt][1] -= int(h/2)

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

bpy.data.objects["myMesh_object"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["myMesh_object"]

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode( type  = 'FACE'   )
bpy.ops.mesh.select_all( action = 'SELECT' )

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 8)})
bpy.ops.transform.resize(value=(1, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

bpy.ops.object.mode_set( mode = 'OBJECT' )

bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
bpy.ops.transform.translate(value=(0, 0, -w/5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

deg_rad = 3.141592554 / 180

bpy.ops.transform.rotate(value= 180 * deg_rad, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value= 90 * deg_rad, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

bpy.data.objects["myMesh_object"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["myMesh_object"]
bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
bpy.context.object.modifiers["SimpleDeform"].deform_method = 'BEND'
bpy.context.object.modifiers["SimpleDeform"].origin = bpy.data.objects["Empty"]

bpy.context.object.modifiers["SimpleDeform"].angle = -55 * deg_rad
bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Y'

bpy.ops.transform.resize(value=(1.2, 1, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

# blend_file_path = bpy.data.filepath
# directory = os.path.dirname(blend_file_path)
# target_file = os.path.join(directory, 'myfile.obj')

bpy.ops.export_scene.obj(filepath = path + '\\myfile.obj')