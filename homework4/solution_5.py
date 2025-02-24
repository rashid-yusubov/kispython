import math


def main(n):
    return (
        -0.06 if n == 0 else
        0.31 if n == 1 else
        math.cos(main(n - 1)) ** 3 - main(n - 2) ** 2 - 1
    )
