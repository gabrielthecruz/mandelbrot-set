import itertools
import numpy as np
from PIL import Image

WIDTH, HEIGHT = (400, 300)
MAX_ITERATIONS = 20
COLORS = [
    (0, 0, 0), (25, 25, 25), (50, 50, 50),
    (76, 76, 76), (102, 102, 102), (127, 127, 127),
    (153, 153, 153), (178, 178, 178), (204, 204, 204),
    (229, 229, 229)
]


def gen_pixels(width, height):
    '''Yields a (x, y) pair with the coordinates of each pixel.'''
    x = range(1, width)
    y = range(1, height)

    for pixel in itertools.product(x, y):
        yield pixel


def gen_coords(min_x, max_x, min_y, max_y, width, height):
    '''Yields the coordinate of each point of the Mandelbrot set.'''
    x_axis = np.linspace(min_x, max_x, num=width)
    y_axis = np.linspace(min_y, max_y, num=height)

    for coord in itertools.product(x_axis, y_axis):
        yield coord


def gen_iterations(pixels, coords, depth=10):
    '''Yields the number of iterations of each pixel.'''
    for pixel, coord in zip(pixels, coords):
        scaled_x, scaled_y = coord
        x, y = coord

        for iteration in range(depth):
            x = (x*x) - (y*y) + scaled_x
            y = (2 * x * y) + scaled_y

            if abs(x*x) + abs(y*y) > 4:
                break

        yield pixel, iteration


def gen_hist_colors(pixel_iterations):
    '''Yields the pixel and its color.'''
    for pixel, color_index in pixel_iterations:
        if color_index == MAX_ITERATIONS - 1:
            color = (0, 0, 0)
        else:
            color = (255, 255, 255)
        yield pixel, color


def plot_on_image(image, pixels):
    '''Draws the color on the pixel coordinates on image.'''
    for pixel, color in pixels:
        image.putpixel(pixel, color)


pixels = gen_pixels(WIDTH, HEIGHT)
coords = gen_coords(-2, 2, -1, 1, WIDTH, HEIGHT)
iterations = gen_iterations(pixels, coords)
colors = gen_hist_colors(iterations)

image = Image.new('RGB', (WIDTH, HEIGHT))

plot_on_image(image, colors)

image.save('mandelbot.jpg')