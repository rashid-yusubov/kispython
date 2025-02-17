import math


def recursive_sum(c, m, n, a, x):
    if c > a:
        return 0
    result = 0
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            term = (
                65 * math.cos(j) ** 6
                - 61 * c ** 6
                - 38 * (59 - i ** 3 - x) ** 4
            )
            result += term
    return result + recursive_sum(c + 1, m, n, a, x)


def main(n, m, a, x):
    return recursive_sum(1, m, n, a, x)
