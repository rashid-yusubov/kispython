import math
from math import floor, sqrt


def main(x, y, z):
    term1 = y ** 2
    term2 = 11 * (floor(z ** 3 - 32 * x)) ** 6
    term3 = 34 * (sqrt(38 * z ** 2)) ** 6
    term4 = floor(y - 83 * x ** 3 - 67) ** 4

    return term1 - term2 - (term3 + term4)
