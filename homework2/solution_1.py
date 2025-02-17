import math


def main(z):
    if z < 109:
        return math.log10(1 + z / 65 + z**3)

    elif 109 <= z < 121:
        return 90 * (z**3 + z**2 + 1) + math.log(z)

    else:
        arctg = math.atan(z**2 - 19 - (z**3 / 8))
        return 92 + 60 * math.log10(z) ** 2 + 34 * (arctg) ** 3
