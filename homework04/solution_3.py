import math


def main(n):
    dp = [-0.06, 0.31] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = math.cos(dp[i - 1]) ** 3 - dp[i - 2] ** 2 - 1
    return dp[n]
