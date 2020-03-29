import os
path = os.path.dirname(os.path.abspath(__file__))
os.system("blender --background --python " + path + "\\printapic.py")