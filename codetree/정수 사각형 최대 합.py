n = int(input())
mat = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
dp = [[0] * (n + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = mat[i][j] + max(dp[i][j - 1], dp[i - 1][j])

print(dp[n][n])
