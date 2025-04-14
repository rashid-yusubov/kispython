def helper(i, x, y, z, n):
    if i > n:
        return 0
    term = (y[n - i] ** 2 + 75 * x[(i - 1) // 2] ** 3 + 47 * z[i - 1]) ** 4
    return term + helper(i + 1, x, y, z, n)


def main(x, y, z):
    return 77 * helper(1, x, y, z, len(x))
