def main(x, y, z):
    n = len(x)
    result = 0.0
    for i in range(1, n + 1):
        term = (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
        result += term
    return 77 * result
