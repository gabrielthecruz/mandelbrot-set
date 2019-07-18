import matplotlib.pyplot as plt
import numpy as np


def check(coordinate, iterations):
    # coordinate = x + y * 1j
    results = [0]
    is_valid = True

    for _ in range(iterations):
        result = results[-1] ** 2 + coordinate

        conditions = [
            result.real > 2,
            result.imag > 2,
            result in results
        ]
        
        results.append(result)
        if any(conditions):
            is_valid = False
            break

    return is_valid, results[-1], len(results)


def get_coords(x_interval, i_interval, precision=1):
    step = 1 / 10 ** precision
    x = np.arange(*x_interval, step)
    i = np.arange(*i_interval, step, dtype=complex) * 1j

    x_axis, i_axis = np.meshgrid(x, i, indexing='ij', sparse=True)
    coordinates = (x_axis + i_axis).round(precision)
    
    return coordinates


def export_coords(header, *args, filename='coords.csv'):
    
    # for a,b,c,d in :
    #     print(a,b,c,d)
    #     break
    types = [complex, bool, complex, int]
    data = np.array(list(np.nditer(args)), dtype='<c16,<i4,<c16,<i4')  # |b1
    print(data.dtype)
    np.savetxt(filename, data, header=','.join(header), delimiter=',',
               encoding='utf-8', fmt=['%.3f %+.3c', '%d', '%.3f %+.3c', '%d'])  # 


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

    coords = get_coords(x, y, 1).ravel()
    check_array = np.vectorize(check)
    # check_array = np.frompyfunc(check, 2, 3, dtype=[bool, complex, int])
    result = check_array(coords, 20)
    header = ('Coordenadas', 'Ativo', 'Resultado', 'Iteracao')

    export_coords(header, coords, *result, filename='test.csv')
    
    # fig, ax = plt.subplots()
    # print_x = np.where(result[0] == True, coords.real, None)
    # print_y = np.where(result[0] == True, coords.imag, None)
    # ax.plot(print_x, print_y, ',-', color='black')
    # plt.show()


if __name__ == '__main__':
    main()
