import math


def main(n):
    sign = n
    match sign:
        case 0:
            return -0.06
        case 1:
            return 0.31

    return (math.cos(main(n - 1)) ** 3 - main(n - 2) ** 2 - 1)
