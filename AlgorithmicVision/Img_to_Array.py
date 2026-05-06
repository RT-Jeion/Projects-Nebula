import cv2
import csv
import numpy as np

image_path = "nothing_happend.jpg"
z = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
print(f"Image successfully loadeded. Dimension: {z.shape[1]}x{z.shape[0]}")
height, width = z.shape
x_cor, y_cor = np.meshgrid(np.arange(width), np.arange(height))

x_flat = x_cor.flatten()
y_flat = y_cor.flatten()
z_flat = z.flatten()


points = np.column_stack((x_flat, y_flat, z_flat))

if __name__=="__main__":
    print(z)
    print(points)