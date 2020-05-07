from flask import Flask, render_template, url_for, request, redirect, flash
import os
from werkzeug.utils import secure_filename
import cv2
import bpy
import numpy as np
import math

path = os.path.dirname(os.path.abspath(__file__))
print(path)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = path + '\\images'

def printapic(filename):

    max_kpx = 150
    scale = 0.15
    extrude_amt = 8.5

    img = cv2.imread(path + "\\images\\" + filename)
    h, w, _ = img.shape
    max_px = max_kpx * 1000

    if h * w > max_px:

        scale_percent = max_px / (h * w)
        w_down = int(w * math.sqrt(scale_percent))
        h_down = int(h * math.sqrt(scale_percent))
        img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
        w, h = w_down, h_down

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    vertsData = []
    for j in range(h):
        for i in range(w):
            vertsData.append([i - w/2, j - h/2, img[j,i] / 16]) # **.3

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

    bpy.ops.object.delete(use_global=False)
    mesh = bpy.data.meshes.new("myMesh_mesh")
    mesh.from_pydata(vertsData, [], facesData)

    new_object = bpy.data.objects.new("myMesh_object", mesh)
    new_object.data = mesh
    bpy.context.collection.objects.link(new_object) # 2.8

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

    # if mode == 'panorama':
    #     bpy.context.object.modifiers["SimpleDeform"].angle = 6.28319

    bpy.ops.transform.resize(value=(scale, scale, scale), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.rotate(value= -90*deg_rad, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    name = os.path.splitext(image)[0]
    bpy.ops.export_mesh.stl(filepath = path + '\\results\\' + name + '.stl')

    return "neat"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        extension = os.path.splitext(filename)[1]
        if len(filename) > 13:
            filename = filename[0:10] + extension
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return printapic(filename)
        else:
            return render_template('index.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)



# os.system("blender --background --python " + path + "\\printapic.py")
# blender --background --python rebuild.py