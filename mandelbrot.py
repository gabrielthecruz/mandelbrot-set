from matplotlib import colors
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd 
import matplotlib


def check(c_number, iterations):
    results = [0]

    for i in range(iterations):
        result = results[-1] ** 2 + c_number

        if result.real > 2 or result.imag > 2:
            return False, i
        elif result in results:
            break
        
        results.append(result)
    
    return True, None


def points(min_x, max_x, min_y, max_y):
    for x in np.arange(min_x, max_x, 0.001):
        for y in np.arange(min_y, max_y, 0.001):
            yield round(x, 3) + (round(y, 3) * 1j)


def export_points():
    import csv

    x = (-2, 0.5)
    y = (-1, 1)
    i = 20
    colors = 'yyyyyooooorrrrrbbbbb'

    with open('points_bkp.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(('x', 'y', 'color'))

        for coord in points(x[0], x[1], y[0], y[1]):
            is_valid, stop_iter = check(coord, i)
            color = 'k' if is_valid else colors[stop_iter]
            csv_writer.writerow(coord.real, coord.imag, color)


def read_points(ax):
    import pandas as pd

    points = pd.read_csv('points_bkp.csv', sep='\t')
    colors = points['color'].unique()

    for color in colors:
        f_points = points[points.color == color]
        ax.plot(f_points['x'], f_points['y'], ',-', color=color)

    return ax


def main():
    fig, ax = plt.subplots()
    
    ax.set_xticks([-2, -1, 0, 1])
    ax.set_yticks([-1, 0, 1])

    ax = read_points(ax)
    plt.show()


if __name__ == '__main__':
    main()
