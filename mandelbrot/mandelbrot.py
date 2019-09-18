from collections import namedtuple
from PIL import Image
import numpy as np
import math


def gen_palette(ncolors):
    red = np.linspace(0, 15, num=ncolors)
    green = np.linspace(16, 92, num=ncolors)
    blue = np.linspace(23, 232, num=ncolors)

    return list(zip(red, green, blue))


def check(coord, max_iter, callback=None):
    x, y = coord.x, coord.y
    xsqr, ysqr, zsqr = 0, 0, 0

    for iter_n in range(max_iter):
        x = xsqr - ysqr + coord.x
        y = zsqr - xsqr - ysqr + coord.y
        xsqr = x ** 2
        ysqr = y ** 2
        zsqr = (x + y) ** 2

        if xsqr + ysqr > 4:
            break

    if callback is not None:
        iter_n = callback(iter_n, x, y, max_iter)

    return iter_n


def get_coords(x_range, i_range, width, height):
    real = np.linspace(*x_range, num=width)
    imag = np.linspace(*i_range, num=height)
    Point = namedtuple('Point', ['x', 'y'])

    for px, x in enumerate(real):
        for py, y in enumerate(imag):
            yield Point(px, py), Point(x, y)


def smooth_coloring(iterations, x, y, max_iterations):
    if iterations + 1 < max_iterations:
        log_xy = math.log(x*x + y*y) / 2
        v_xy = math.log(log_xy / math.log(2)) / math.log(2)
        iterations -= v_xy

    return iterations


def main():
    x = (-2.2, 0.8)
    y = (-1.2, 1.2)
    width = 800
    height = 600
    image = Image.new('RGB', (width, height))
    max_iterations = 100
    palette = gen_palette(max_iterations)

    for pixel, coord in get_coords(x, y, width, height):
        n = check(coord, max_iterations, callback=smooth_coloring)

        color1 = palette[math.ceil(n)]
        color2 = palette[(math.ceil(n) + 1) % max_iterations]

        color = tuple(int(color1[i] + n%1 * (color2[i] - color1[i])) for i in range(3))

        image.putpixel(pixel, color)

    image.save('../mandelbrot.png', 'PNG')


if __name__ == '__main__':
    main()
