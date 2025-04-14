import math


def main(x, y, z):
    term1 = y ** 2
    term2 = 11 * (math.floor(z ** 3 - 32 * x)) ** 6
    term3 = 34 * (math.sqrt(38 * z ** 2)) ** 6
    term4 = math.floor(y - 83 * x ** 3 - 67) ** 4

    return term1 - term2 - (term3 + term4)
