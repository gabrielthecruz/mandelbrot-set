def check_point(c, iterations=10):
    print(c)
    r = 0
    results = set()
    for i in range(iterations):
        r = r ** 2 + c
        results.add(r)
        if (r.real > 2 or r.imag > 2) or (r.real <= -2 or r.imag <= -2):
            break
    else:
        return results
    
    return set()


# c = -1j
# func = get_mandelbrot(c)
# r = {0j}
# coords = {(0,0)}
# lr = 0
# for _ in range(100):
#     x = func(lr)
#     lr = x
#     r.add(x)
#     coords.add((x.real, x.imag))

# print(r)
# print(coords)
