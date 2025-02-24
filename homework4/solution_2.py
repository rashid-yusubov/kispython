import math


def recurrence_generator():
    yield -0.06  # f(0)
    yield 0.31   # f(1)
    fn_minus_2 = -0.06
    fn_minus_1 = 0.31
    while True:
        fn = math.cos(fn_minus_1) ** 3 - fn_minus_2 ** 2 - 1
        yield fn
        fn_minus_2, fn_minus_1 = fn_minus_1, fn


def main(n):
    gen = recurrence_generator()
    result = None
    for _ in range(n + 1):
        result = next(gen)
    return result
