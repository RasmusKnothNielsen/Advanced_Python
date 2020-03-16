
from PIL import Image
from array import array

xmin, xmax = -2, 0.8
ymin, ymax = -1.5, 1.5

max_iter = 200

width, height = 400, 400

pix = lambda x, y: x + y * width
# The following line is the equivalent of the map function in Processing
cmap = lambda value, v_min, v_max, p_min, p_max: p_min + (p_max - p_min) * ((value - v_min)/(v_max - v_min))

m = array('B', [0] * width * height)

for cx in range(width):
    for cy in range(height):
        cr = cmap(cx, 0, width, xmin, xmax)
        ci = cmap(cy, 0, height, ymin, ymax)
        c = cr + ci * 1j    # Creating the complex number
        z = 0 + 0j
        for i in range(max_iter):
            z = z * z + c
            if abs(z) > 2:
                m[pix(cx, cy)] = 255
                break
        else:
            m[pix(cx, cy)] = 0

# Mode L is a black and white picture
img = Image.new('L', (width, height))
img.frombytes(m.tobytes())
img.save("Mandelbrot.jpg")