import math


def main(z):
    conditions = [
        (
            lambda z: z < 109,
            lambda z: math.log10(1 + z / 65 + z**3)
        ),
        (
            lambda z: 109 <= z < 121,
            lambda z: 90 * (z**3 + z**2 + 1) + math.log(z)
        ),
        (
            lambda z: z >= 121,
            lambda z: (
                92 +
                60 * math.log10(z) ** 2 +
                34 * (math.atan(z**2 - 19 - (z**3 / 8))) ** 3
            )
        )
    ]

    return next(
        func(z)
        for condition, func in conditions
        if condition(z)
    )
