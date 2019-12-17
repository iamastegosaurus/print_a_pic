import bpy
import csv
import math

x = []
y = []
z = []

with open('Q:\\print_a_pic\\rend\\data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        x.append(float(row[0]))
        y.append(float(row[1]))
        z.append(float(row[2]))

for t in range(len(z)):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(x[t], y[t], z[t] / 32))
    if t % 50 == 0:
        print(t / len(z))
