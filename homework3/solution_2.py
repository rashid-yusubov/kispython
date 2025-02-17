import math


def main(n, m, a, x):
    return sum(
        65 * math.cos(j) ** 6 - 61 * c ** 6 - 38 * (59 - i ** 3 - x) ** 4
        for c in range(1, a + 1)
        for j in range(1, m + 1)
        for i in range(1, n + 1)
    )
