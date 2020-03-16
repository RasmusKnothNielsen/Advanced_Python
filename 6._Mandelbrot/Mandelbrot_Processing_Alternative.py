# Paste the following into Processing

import time

xmin, xmax = -2, 0.8
ymin, ymax = -1.5, 1.5

max_iter = 200

screen_width, screen_height = 400, 400


def pix(x, y):
    return x + y * width


def setup():
    t0 = time.time()

    size(screen_width, screen_height)

    loadPixels()
    for cx in range(width):
        for cy in range(height):
            cr = map(cx, 0, width, xmin, xmax)
            ci = map(cy, 0, height, ymin, ymax)

            c = complex(cr, ci)
            z = complex(0, 0)
            for i in range(max_iter):
                z = z * z + c
                if abs(z) > 2:
                    # Pixel is outside Mandelbrot
                    pixels[pix(cx, cy)] = color(255)  # Color the pixel white
                    break
            else:
                if abs(z) > 0.30:
                    pixels[pix(cx, cy)] = color(200, 62, 120)
                elif abs(z) > 0.20:
                    pixels[pix(cx, cy)] = color(100, 63, 230)
                elif abs(z) > 0.10:
                    pixels[pix(cx, cy)] = color(50, 23, 130)
                else:
                    pixels[pix(cx, cy)] = color(0)

    updatePixels()
    t1 = time.time()
    print("Time: %s") % str(t1 - t0)[:4]