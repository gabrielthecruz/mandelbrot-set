from itertools import product
from PIL import Image
import numpy as np
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __iter__(self):
        return iter([self.x, self.y])


class Pixel(Point):
    pass


class Coordinate(Point):
    pass


def coordinates(min_x, max_x, min_y, max_y, width, height):
    '''Yields a pixel and a coordinate.'''
    x_axis = np.linspace(min_x, max_x, num=width)
    y_axis = np.linspace(min_y, max_y, num=height)

    for (px, x), (py, y) in product(enumerate(x_axis), enumerate(y_axis)):
        yield Pixel(px, py), Coordinate(x, y)


def bulb_checking(coord):
    '''Performs the bulb checking for optimization.'''
    x, y = coord
    sqr_y = y ** 2
    q = (x - 0.25) ** 2 + sqr_y

    return q * (q + x - 0.25) <= 0.25 * sqr_y


def escape_time(coord, max_iter):
    '''
    Executes escape time algorithm on coord.
    Returns the last iteration number, x and y values calculated.
    '''
    sqr_x, sqr_y, sqr_z = 0, 0, 0

    for iteration in range(1, max_iter + 1):
        x = sqr_x - sqr_y + coord.x
        y = sqr_z - sqr_x - sqr_y + coord.y

        sqr_x = x ** 2
        sqr_y = y ** 2
        sqr_z = (x + y) ** 2

        if sqr_x + sqr_y > 4:
            break

    return iteration, x, y


def smooth_coloring(iter_n, x, y, max_iters):
    '''Generates a color.'''
    if iter_n < max_iters:
        log_z = math.log(x ** 2 + y ** 2) / 2
        log_2 = math.log(2)
        iter_n += 1 - math.log(log_z / log_2) / log_2

    hue = int(255 * iter_n / max_iters)
    saturation = 255
    value = 255 if iter_n < max_iters else 0

    return (hue, saturation, value)


def mandelbrot(min_x, max_x, min_y, max_y, max_iters, image):
    '''Draws the Mandelbrot Set on image.'''
    width, height = image.size

    for pixel, coord in coordinates(min_x, max_x, min_y, max_y, width, height):
        if bulb_checking(coord):
            color = (0, 0, 0)

        else:
            iteration, x, y = escape_time(coord, max_iters)
            color = smooth_coloring(iteration, x, y, max_iters)

        image.putpixel(tuple(pixel), color)

    return image


if __name__ == '__main__':
    image = Image.new('HSV', (800, 600))
    image = mandelbrot(-2.2, 0.8, -1.2, 1.2, 100, image)
    image.convert('RGB').save('../mandelbrot.png', 'PNG')
