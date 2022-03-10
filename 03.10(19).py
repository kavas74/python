def f(c=-10, d=137):
    if c < 0:
        return c + d
    else:
        return [d] * round(c ** (1 / 3))
