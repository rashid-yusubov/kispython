def main(x, y, z):
    n = len(x)
    return 77 * sum(
        (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
        for i in range(1, n + 1)
    )
