import math


def main(n, m, a, x):
    result = 0
    c = 1
    while c <= a:
        j = 1
        while j <= m:
            i = 1
            while i <= n:
                term = (
                    65 * math.cos(j) ** 6
                    - 61 * c ** 6
                    - 38 * (59 - i ** 3 - x) ** 4
                )
                result += term
                i += 1
            j += 1
        c += 1
    return result
