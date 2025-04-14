import math
import bisect


def main(z):
    limits = [109, 121]
    funcs = [
        lambda z: math.log10(1 + z / 65 + z**3),
        lambda z: 90 * (z**3 + z**2 + 1) + math.log(z),
        lambda z: 92 + 60 * math.log10(z) ** 2 +
        34 * (math.atan(z**2 - 19 - (z**3 / 8))) ** 3,
    ]
    return funcs[bisect.bisect(limits, z)](z)
