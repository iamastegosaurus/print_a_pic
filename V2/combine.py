import cv2
import bpy

img = cv2.imread('Q:\\print_a_pic\\images\\orange.jpg')
h, w, _ = img.shape

# PARAMS

max_px = 500000

if h * w > max_px:
    scale_percent = max_px / (h * w)
    w_down = int(w * scale_percent)
    h_down = int(h * scale_percent)
    img = cv2.resize(img, (w_down, h_down), interpolation = cv2.INTER_AREA)
    w, h = w_down, h_down
    # print('new dim: ' + str(w) + ', ' + str(h))

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


vertsData = []
for i in range(w):
    for j in range(h):
        vertsData.append( [i, j, img[j][i]**.25] )

# print(vertsData[0])

cv2.imshow('new', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


facesData = []

def get_faces():
    for y in range( h-1 ):
        for x in range( w-1 ):
            a = (y) + (x*w)
            b = (y + 1) + (x*w)
            c = (y + 1) + ((x+1) * w)
            d = (y) + ((x+1) * w)
            facesData.append( (a,b,c,d) )

get_faces()

mesh = bpy.data.meshes.new("myMesh_mesh")
mesh.from_pydata(vertsData, [], facesData)
mesh.update()

new_object = bpy.data.objects.new("myMesh_object", mesh)
new_object.data = mesh
bpy.context.collection.objects.link(new_object)