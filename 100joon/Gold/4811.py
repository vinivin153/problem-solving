import sys

input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break

    dp = [[0] * 31 for _ in range(31)]

    for i in range(1, 31):
        dp[0][i] = 1

    for i in range(1, 31):
        for j in range(30):
            if j == 0:
                dp[i][j] = dp[i - 1][j + 1]
            else:
                dp[i][j] = dp[i - 1][j + 1] + dp[i][j - 1]

    print(dp[n][0])
