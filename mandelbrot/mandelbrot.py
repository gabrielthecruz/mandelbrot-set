from collections import namedtuple
from PIL import Image
import numpy as np


def check(coord, max_iter):
    x, y = coord.x, coord.y

    for iter_n in range(max_iter):
        x, y = x*x - y*y + coord.x, 2*x*y + coord.y

        if x*x + y*y > 4:
            break

    return iter_n


def get_coords(x_range, i_range, width, height):
    real = np.linspace(*x_range, num=width)
    imag = np.linspace(*i_range, num=height)
    Point = namedtuple('Point', ['x', 'y'])

    for px, x in enumerate(real):
        for py, y in enumerate(imag):
            yield Point(px, py), Point(x, y)


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
