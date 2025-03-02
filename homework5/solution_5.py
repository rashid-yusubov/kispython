def main(x, y, z):
    n = len(x)
    result = 0.0
    i = 1

    while i <= n:
        term = (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
        result += term
        i += 1

    return 77 * result
