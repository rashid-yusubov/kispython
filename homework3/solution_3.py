from math import cos, pow
from functools import reduce


def main(n, m, a, x):
    return reduce(
        lambda acc_c, c: acc_c + reduce(
            lambda acc_j, j: acc_j + reduce(
                lambda acc_i, i: acc_i + (
                    65 * pow(cos(j), 6) - 61 * pow(c, 6) -
                    38 * pow(59 - pow(i, 3) - x, 4)
                ),
                range(1, n + 1),
                0
            ),
            range(1, m + 1),
            0
        ),
        range(1, a + 1),
        0
    )
