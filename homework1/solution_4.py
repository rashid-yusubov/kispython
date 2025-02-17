from math import floor, sqrt


def main(x, y, z):
    return (
        y ** 2
        - 11 * (floor(z ** 3 - 32 * x)) ** 6
        - (34 * (sqrt(38 * z ** 2)) ** 6
           + floor(y - 83 * x ** 3 - 67) ** 4)
    )
