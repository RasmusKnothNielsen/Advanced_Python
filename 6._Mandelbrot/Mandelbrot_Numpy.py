from PIL import Image
import numpy as np

width, height = 400, 400
xmin, xmax = -2, 0.8
ymin, ymax = -1.5, 1.5

max_iter = 200

# The following line is the equivalent of the map function in Processing
cmap = lambda value, v_min, v_max, p_min, p_max: p_min + (p_max - p_min) * ((value - v_min)/(v_max - v_min))

# Make an numpy array with zeroes, that is width times height large.
# use the datatype of np.complex_ to get the highest precision complex number possible
C = np.zeros((width, height), dtype=np.complex_)
Z = np.zeros((width, height), dtype=np.complex_)
M = np.zeros((width, height))

for cx in range(width):
    for cy in range(height):
        cr = cmap(cx, 0, width, xmin, xmax)
        ci = cmap(cy, 0, height, ymin, ymax)
        C[cx][cy] = cr + ci * 1j


# Separating the two loops, transform the operation from big O^3 to big O^2
for i in range(max_iter):
    N = np.less(abs(Z), 2)  # Only save the elements that are lower than 2,and thus inside Mandelbrot set
    Z[N] = Z[N] * Z[N] + C[N]
    M[N & (abs(Z) > 2)] = 255

    # Since the default value is zero, we do not have to set the rest

img = Image.fromarray(np.uint8(M.T))
img.save("MandelbrotNumpy.jpg")
