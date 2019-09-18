from collections import namedtuple
from PIL import Image, ImageColor
import numpy as np
import math


def check(coord, max_iter, callback=None):
    x, y = coord.x, coord.y
    xsqr = 0
    ysqr = 0
    zsqr = 0

    for iter_n in range(max_iter):
        # x, y = x*x - y*y + coord.x, 2*x*y + coord.y
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
        iterations += 1 - v_xy

    return iterations


def main():
    x = (-2.2, 0.8)
    y = (-1.2, 1.2)
    width = 800
    height = 600
    image = Image.new('RGB', (width, height))

    for pixel, coord in get_coords(x, y, width, height):
        n = check(coord, 100)

        red = 0 if n < 99 else 255
        green = 0 if n < 99 else 255
        blue = 0 if n < 99 else 255

        image.putpixel(pixel, (red, green, blue))

    image.save('../mandelbrot.png', 'PNG')


if __name__ == '__main__':
    main()
