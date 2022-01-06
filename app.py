import cv2
import bpy
import numpy as np
import os
import math

filename = 'combo_crop.jpg'
path = os.path.dirname(os.path.abspath(__file__))
img = cv2.imread(path + '\\img\\' + filename, 0)
h, w = img.shape

border = True
curve = False

target_width_x = 50 # in mm, scale just driven off width rn
# derived_width_y = target_width_x * h / w
# max_px = target_width_x * 22 * derived_width_y * 22
# print(max_px)
max_px = 1000000 # 1920x1080 img is 2 mil pixels, maximum 2560x1440 is 3.7 mil pixels, if using whole buildplate (115x65)
# ANYCUBIC LCD 22 PX/MM

scale_percent = max_px / (h * w)
w_down = int(w * math.sqrt(scale_percent))
h_down = int(h * math.sqrt(scale_percent))
img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
w, h = w_down, h_down

# img = cv2.blur(img, ksize=(3,3))

# cv2.imshow('img', img)
# cv2.waitKey(0)

big_px = cv2.minMaxLoc(img)[1]
smol_px = cv2.minMaxLoc(img)[0]

border_width_mm = 4 # true mm values 
angle_width_mm = 2
border_thicc_mm = 1
face_norm_mm = 1

non_border_width = target_width_x - 2 * (border_width_mm)
scale = non_border_width / w

extrude_amt = (border_thicc_mm + 2) / scale

border_width = border_width_mm / scale
angle_width = angle_width_mm / scale
border_thicc = border_thicc_mm / scale


def get_points():
    points = []
    for j in range(h):
        for i in range(w):
            norm = ( (img[j,i] - smol_px) / (big_px - smol_px) ) * (face_norm_mm / scale)
            points.append([i - w/2, j - h/2, norm]) 

    if border == True:
        points.append([-w/2 - angle_width, -h/2 - angle_width, -border_thicc])
        points.append([w/2 + angle_width, -h/2 - angle_width, -border_thicc])
        points.append([w/2 + angle_width, h/2 + angle_width, -border_thicc])
        points.append([-w/2 - angle_width, h/2 + angle_width, -border_thicc])

        points.append([-w/2 - border_width, -h/2 - border_width, -border_thicc])
        points.append([w/2 + border_width, -h/2 - border_width, -border_thicc])
        points.append([w/2 + border_width, h/2 + border_width, -border_thicc])
        points.append([-w/2 - border_width, h/2 + border_width, -border_thicc])

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

    if border == True:

        sp = w*h
        
        tl = 0
        tr = w-1
        br = w*h-1
        bl = w*(h-1)
        
        faces.append( (sp, sp+1, tr,) )
        faces.append( (tr, tl, sp) )

        faces.append( (sp+1, sp+2, br,) )
        faces.append( (br, tr, sp+1) )

        faces.append( (sp+2, sp+3, bl,) )
        faces.append( (bl, br, sp+2) )

        faces.append( (sp+3, sp, tl) )
        faces.append( (tl, bl, sp+3) )

        
        tl = sp
        tr = sp+1
        br = sp+2
        bl = sp+3
        sp += 4

        faces.append( (sp, sp+1, tr,) )
        faces.append( (tr, tl, sp) )

        faces.append( (sp+1, sp+2, br,) )
        faces.append( (br, tr, sp+1) )

        faces.append( (sp+2, sp+3, bl,) )
        faces.append( (bl, br, sp+2) )

        faces.append( (sp+3, sp, tl) )
        faces.append( (tl, bl, sp+3) )

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

if curve == True: # only curves litho, not border rn
    # might be because just two triangles for each border
    bpy.ops.object.modifier_add(type='SIMPLE_DEFORM')
    bpy.context.object.modifiers["SimpleDeform"].deform_method = 'BEND'
    bpy.context.object.modifiers["SimpleDeform"].origin = bpy.data.objects["Empty"]
    bpy.context.object.modifiers["SimpleDeform"].angle = -45 * deg_rad
    bpy.context.object.modifiers["SimpleDeform"].deform_axis = 'Y'

bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.transform.rotate(value= -90*deg_rad, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

name = os.path.splitext(filename)[0]
bpy.ops.export_mesh.stl(filepath = path + '\\res\\' + name + '.stl')
