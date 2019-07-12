from matplotlib import colors
import matplotlib.pyplot as plt

import numpy as np
import matplotlib


def check_point(c, iterations=10):
    r = 0
    results = set()
    for i in range(iterations):
        r = r ** 2 + c

        if r.real > 2 or r.imag > 2:
            return False
        elif r in results:
            break

        results.add(r)
    
    return True


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
            yield x + (y * 1j)


fig, ax = plt.subplots()
colors = ['k'] * 5 + ['y'] * 5 + ['r'] * 5 + ['b'] * 5
colors = 'kyrbb'
for c_number in points(-2, 0.5, -1, 1):
    is_valid, stop_iter = check(c_number, 5)
    color = 'k' if is_valid else colors[stop_iter]

    ax.plot(c_number.real, c_number.imag, color + ',-')

plt.show()
