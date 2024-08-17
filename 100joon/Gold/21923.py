import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

dp1 = [[0] * (m) for _ in range(n)]
dp2 = [[0] * (m) for _ in range(n)]

dp1[n - 1][0] = mat[n - 1][0]
for i in range(n - 2, -1, -1):
    dp1[i][0] = mat[i][0] + dp1[i + 1][0]
for i in range(1, m):
    dp1[n - 1][i] = mat[n - 1][i] + dp1[n - 1][i - 1]

dp2[n - 1][m - 1] = mat[n - 1][m - 1]
for i in range(n - 2, -1, -1):
    dp2[i][m - 1] = mat[i][m - 1] + dp2[i + 1][m - 1]
for i in range(m - 2, -1, -1):
    dp2[n - 1][i] = mat[n - 1][i] + dp2[n - 1][i + 1]

for i in range(n - 2, -1, -1):
    for j in range(1, m):
        dp1[i][j] = max(dp1[i][j - 1], dp1[i + 1][j]) + mat[i][j]

for i in range(n - 2, -1, -1):
    for j in range(m - 2, -1, -1):
        dp2[i][j] = max(dp2[i][j + 1], dp2[i + 1][j]) + mat[i][j]

ans = -1 * sys.maxsize
dp = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        dp[i][j] = dp1[i][j] + dp2[i][j]
        if dp[i][j] > ans:
            ans = dp[i][j]

print(ans)
