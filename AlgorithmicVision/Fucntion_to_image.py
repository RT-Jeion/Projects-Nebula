import csv
import numpy as np
import cv2

with open("Params.csv", 'r') as f:
    a = 0 
    for i in csv.reader(f):
        if a == 1:
            p = [float(a) for a in i]
        a += 1

a1 = p[0]
a2 = p[1]
a3 = p[2]
a4 = p[3]
a5 = p[4]
a6 = p[5]

width = 2552
height = 4096 
print("Generating Grids....")

x, y = np.meshgrid(np.arange(width), np.arange(height))

z_arr = (
    a1 * (x**2) + 
    a2 * (y**2) +
    a3 * x * y  +
    a4 * x +
    a5 * 5 +
    a6
)

z_min = np.min(z_arr)
z_max = np.max(z_arr)

z_nor = (255 * (z_arr - z_min) / (z_max - z_min)).astype(np.uint8)

print(z_arr)
print(z_nor)

#new_file = "zoro.jpg"
#cv2.imwrite(new_file, z_nor)