import sys

input = sys.stdin.readline

h, n = map(int, input().split())
m = abs(h - n)
dp = [[0] * (m + 1) for _ in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = 1

for i in range(1, m + 1):
    for j in range(1, i + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[m][m])
