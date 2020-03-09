# Insert into Processing

MAX_ITER = 10

WIDTH = 512
HEIGHT = 512


def mandelbrot(c):
    z = 0
    n = 0
    while abs(z) <= 2 and n < MAX_ITER:
        z = z * z + c
        n += 1
    return n


# Map pixels from -2 to 2
# pixels = {(0, 102): -2, (103, 206) -1, (207, 300) 0, (301, 402) 1, (403, 512) 2)}

# map the point from -2 to 2, but convert it to a number between 0 and 512
# map(punktet, -2, 2, 0, 512)

def setup():
    size(WIDTH, HEIGHT)
    for a in range(0, 512, 1):
        for b in range(0, 512, 1):
            real = map(a, 0, 512, -2, 2)
            imaginary = map(b, 0, 512, -2, 2)
            c = complex(real, imaginary)
            # print(c, mandelbrot(c))
            if mandelbrot(c) == MAX_ITER:
                point(a, b)
    print("Done painting")

