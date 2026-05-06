import numpy as np
import csv
from scipy.optimize import curve_fit

from Img_to_Array import points

x_axis = points[:, 0]
y_axis = points[:, 1]
z_axis = points[:, 2]

def surface(coords, a1, a2, a3, a4, a5, a6):
    x,y = coords
    return a1 * (x**2) + a2 * (y**2) + a3 * x * y + a4 * x + a5 * y + a6


xy_data = np.vstack((x_axis, y_axis))

initial_guess = [1,1,1,1,1,1]

params, covariance = curve_fit(surface, xy_data,z_axis, p0=initial_guess)

formatted = np.array([np.format_float_positional(p, unique=True) for p in params])

with open("Params.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["a1","a2","a3","a4","a5","a6"])
    writer.writerow(formatted)