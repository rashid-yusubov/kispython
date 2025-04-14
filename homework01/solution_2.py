import math


def main(x, y, z):
    return (
        y ** 2
        - 11 * (math.floor(z ** 3 - 32 * x)) ** 6
        - (34 * (math.sqrt(38 * z ** 2)) ** 6
           + math.floor(y - 83 * x ** 3 - 67) ** 4)
    )
