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


def points(min_x, max_x, min_y, max_y):
    for x in np.arange(min_x, max_x, 0.001):
        for y in np.arange(min_y, max_y, 0.001):
            yield x + y * 1j


fig, ax = plt.subplots()
for z in points(-2, 0.5, -1, 1):
    if check_point(z, iterations=20):
        ax.plot(z.real, z.imag, 'k,-')
    
plt.show()
