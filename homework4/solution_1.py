import math


def main(n):
    if n == 0:
        return -0.06
    elif n == 1:
        return 0.31
    else:
        return math.cos(main(n - 1)) ** 3 - main(n - 2) ** 2 - 1
