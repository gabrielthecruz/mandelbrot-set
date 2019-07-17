import matplotlib.pyplot as plt
import numpy as np


def check(coordinate, iterations):
    results = np.zeros(iterations, dtype=complex)
    valid_coord = True

    for i in range(1, iterations):
        results[i] = results[i-1] ** 2 + coordinate

        cond1 = results.real > 2
        cond2 = results.imag > 2
        cond3 = results[:i] == results[i]
        if np.any([cond1, cond2, cond3]):
            valid_coord = False
            break

    return valid_coord, results


def get_coords(x_interval, i_interval, precision=1):
    step = 1 / 10 ** precision
    x = np.arange(*x_interval, step)
    i = np.arange(*i_interval, step, dtype=complex) * 1j

    x_axis, i_axis = np.meshgrid(x, i, indexing='ij', sparse=True)
    coordinates = (x_axis + i_axis).round(precision)
    
    return coordinates


def export_coords(coordinates, total, b_results, c_results, filename='coords.csv'):
    file_header = ('coord', 'in', 'iterations', 'last_result')
    data = (coordinates, total, b_results, c_results)
    np.savetxt(filename, data, header=file_header, delimiter=',', newline='\n',
               encoding='utf-8', )



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
    x = (-2, .5)
    y = (-1, 1)

    coords = get_coords(x, y, 1)
    b_results = np.empty(coords.size, dtype=bool)
    total = np.empty(coords.size, dtype=int)
    c_results = np.empty(coords.size, dtype=complex)
    
    for index, coord in enumerate(coords):
        r = check(coord, 20)
        b_results[index] = r[0]
        c_results[index] = r[1][-1]
        total[index] = r[1].size

    export_coords(coords, total, b_results, c_results, 'test.csv')

    # complexes = points(-2, 0.5, -1, 1):
    fig, ax = plt.subplots()

    # x_axis, i_axis, z_axis = np.meshgrid(coords.real, coords.imag, b_results)


    
    # ax = 
    plt.show()


if __name__ == '__main__':
    main()
