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
    data = np.rec.fromarrays(args, names=header)
    data['Resultado'] = data['Resultado'].round(3)

    np.savetxt(filename, data, header=','.join(header), delimiter=',',
               encoding='utf-8', fmt=['%s', '%d', '%s', '%d'])  # 


def read_points(ax):
    filename = 'points_bkp\points3.csv'
    points = np.genfromtxt(filename, delimiter=',', skip_header=1, 
        dtype=(float, float, int), usecols=(0, 1, 2), names=('a', 'b', 'c'))
    
    xs = np.where(points['c'] == 1, points['a'], None)
    ys = np.where(points['c'] == 1, points['b'], None)
    ax.plot(xs, ys, ',-', color='black')


def main():
    x = (-2, .5)
    y = (-1, 1)

    coords = get_coords(x, y, 3).ravel()
    check_array = np.vectorize(check)
    result = check_array(coords, 20)
    header = ('Coordenadas', 'Ativo', 'Resultado', 'Iteracao')

    export_coords(header, coords, *result, filename='test.csv')
    
    fig, ax = plt.subplots()
    print_x = np.where(result[0] == True, coords.real, None)
    print_y = np.where(result[0] == True, coords.imag, None)
    ax.plot(print_x, print_y, ',-', color='black')
    plt.show()


if __name__ == '__main__':
    main()
