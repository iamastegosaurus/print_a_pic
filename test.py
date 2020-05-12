import bpy

def moo():

    for ob in bpy.data.objects:
        print(ob.name)

    bpy.data.objects["Cube"].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects["Cube"]

    bpy.ops.object.delete(use_global=False) 

    for ob in bpy.data.objects:
        print(ob.name)

    return "nothing"


print(moo())