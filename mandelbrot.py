import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors


def np_check(c_number, iterations):
    rs = np.zeros(iterations, dtype=complex)

    for i in range(1, iterations):
        rs[i] = rs[i-1] ** 2 + c_number

        if rs[i].real > 2 and rs.imag > 2:
            break
        elif rs[i] in rs[:i]:
            break
    
    return rs[:i+1]


def points(min_x, max_x, min_y, max_y):
    xs = np.arange(min_x, max_x, 0.001).round(decimals=3)
    ys = np.arange(min_y, max_y, 0.001).round(decimals=3)
    cs = xs + (1j * ys)
    
    return cs


def export_points():
    import csv

    x = (-2, 0.5)
    y = (-1, 1)
    i = 50

    
    with open('points_bkp\points3.csv', 'w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter='\t')
        csv_writer.writerow(('x', 'y', 'mandelbrot?', 'iteração', 'z(n)'))

        for coord in points(x[0], x[1], y[0], y[1]):
            is_valid, stop_iter, zn = check(coord, i)
            
            csv_writer.writerow((coord.real, coord.imag, int(is_valid), stop_iter, zn))


def read_points(ax):
    filename = 'points_bkp\points3.csv'
    points = np.genfromtxt(filename, delimiter='\t', skip_header=1, 
        dtype=(float, float, int), usecols=(0, 1, 2), names=('a', 'b', 'c'))
    
    xs = np.where(points['c'] == 1, points['a'], None)
    ys = np.where(points['c'] == 1, points['b'], None)
    ax.plot(xs, ys, ',-', color='black')


def main():
    # complexes = points(-2, 0.5, -1, 1):
    fig, ax = plt.subplots()
    
    ax = read_points(ax)
    plt.show()


if __name__ == '__main__':
    main()
