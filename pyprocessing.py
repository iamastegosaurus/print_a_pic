import cv2
import bpy
import numpy as np
import os
import math
import sys

filename = sys.argv[1]
path = os.path.dirname(os.path.abspath(__file__))

max_px = 150000
scale = 0.15
extrude_amt = 7.5

img = cv2.imread(path + '\\images\\' + filename, 0)
h, w = img.shape

if h * w > max_px:
    scale_percent = max_px / (h * w)
    w_down = int(w * math.sqrt(scale_percent))
    h_down = int(h * math.sqrt(scale_percent))
    img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
    w, h = w_down, h_down

def get_points():
    points = []
    for j in range(h):
        for i in range(w):
            points.append([i - w/2, j - h/2, img[j,i] ** .25]) 
    
    return points

def get_faces():
    faces = []
    for yy in range( h-1 ):
        for xx in range( w-1 ):
            a = (xx) + (yy*w)
            b = (xx + 1) + (yy*w)
            c = (xx + 1) + ((yy+1) * w)
            d = (xx) + ((yy+1) * w)
            faces.append( (a,b,c) )
            faces.append( (c,d,a) )

    return faces

points = get_points()
faces = get_faces()

bpy.ops.object.delete(use_global=False) 
mesh = bpy.data.meshes.new("myMesh_mesh")
mesh.from_pydata(points, [], faces)

new_object = bpy.data.objects.new("myMesh_object", mesh)
new_object.data = mesh
bpy.context.collection.objects.link(new_object)

bpy.data.objects["myMesh_object"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["myMesh_object"]

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_mode( type  = 'FACE'   )
bpy.ops.mesh.select_all( action = 'SELECT' )

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, extrude_amt)}) 
bpy.ops.transform.resize(value=(1, 1, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

deg_rad = 3.141592554 / 180

bpy.ops.object.mode_set( mode = 'OBJECT' )
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))

bpy.ops.transform.rotate(value= 180 * deg_rad, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value= 90 * deg_rad, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

bpy.data.objects["myMesh_object"].select_set(True)
bpy.context.view_layer.objects.active = bpy.data.objects["myMesh_object"]
bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
bpy.context.object.modifiers["SimpleDeform"].deform_method = 'BEND'
bpy.context.object.modifiers["SimpleDeform"].origin = bpy.data.objects["Empty"]

bpy.context.object.modifiers["SimpleDeform"].angle = -45 * deg_rad
bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Y'

bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value= -90*deg_rad, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

name = os.path.splitext(filename)[0]
bpy.ops.export_mesh.stl(filepath = path + '\\results\\' + name + '.stl')
