import sys

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]
dp[0] = mat[0]


for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j + 1]) + mat[i][j]
        elif j == 1:
            dp[i][j] = max(dp[i - 1]) + mat[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + mat[i][j]

max_value = max(dp[n - 1])
dp[0] = mat[0]
for i in range(1, n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + mat[i][j]
        elif j == 1:
            dp[i][j] = min(dp[i - 1]) + mat[i][j]
        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + mat[i][j]
min_value = min(dp[n - 1])


print(max_value, min_value)
