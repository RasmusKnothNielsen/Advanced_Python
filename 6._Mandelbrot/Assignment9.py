"""
Testing differences in speed with different implementations of the Mandelbrot set.
"""
from PIL import Image
import numpy as np
from numba import jit
from array import array

from numba import jit, vectorize, guvectorize, float64, complex64, int32, float32


@jit(int32(complex64, int32))
def mandelbrot_numba_iteration(c, maxiter):
    nreal = 0
    real = 0
    imag = 0
    for n in range(maxiter):
        nreal = real * real - imag * imag + c.real
        imag = 2 * real * imag + c.imag
        real = nreal;
        if real * real + imag * imag > 4.0:
            return n
    return 0


@guvectorize([(complex64[:], int32[:], int32[:])], '(n),()->(n)', target='parallel')
def mandelbrot_numpy(c, maxit, output):
    maxiter = maxit[0]
    for i in range(c.shape[0]):
        output[i] = mandelbrot_numba_iteration(c[i], maxiter)


def mandelbrot_numba(width, height, maxiter):
    r1 = np.linspace(-2, 0.8, width, dtype=np.float32)
    r2 = np.linspace(-1.5, 1.5, height, dtype=np.float32)
    c = r1 + r2[:, None] * 1j
    n3 = mandelbrot_numpy(c, maxiter)
    return (r1, r2, n3.T)

def MandelbrotNumpy(width, height, max_iterations):

    width, height = width, height
    xmin, xmax = -2, 0.8
    ymin, ymax = -1.5, 1.5

    max_iter = max_iterations

    # The following line is the equivalent of the map function in Processing
    cmap = lambda value, v_min, v_max, p_min, p_max: p_min + (p_max - p_min) * ((value - v_min) / (v_max - v_min))

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

def Mandelbrot(width, height, max_iterations):

    xmin, xmax = -2, 0.8
    ymin, ymax = -1.5, 1.5

    max_iter = max_iterations

    width, height = width, height

    pix = lambda x, y: x + y * 400
    # The following line is the equivalent of the map function in Processing
    cmap = lambda value, v_min, v_max, p_min, p_max: p_min + (p_max - p_min) * ((value - v_min) / (v_max - v_min))

    m = array('B', [0] * width * height)

    for cx in range(width):
        for cy in range(height):
            cr = cmap(cx, 0, width, xmin, xmax)
            ci = cmap(cy, 0, height, ymin, ymax)
            c = cr + ci * 1j  # Creating the complex number
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

if __name__ == "__main__":
    import time

    t0 = time.time()

    Mandelbrot(400, 400, 200)

    t1 = time.time()

    mandelbrot_numba(400, 400, 200)

    t2 = time.time()

    d1 = t1 - t0
    d2 = t2 - t1
    p = ((d2 - d1)/abs(d1))*100
    print("Mandelbrot: " + str(d1))
    print("Mandelbrot using Numba and Jit: " + str(d2))
    print(p)
