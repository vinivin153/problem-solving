import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().rstrip())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

for i in range(m):
    dp[0][i] = mat[0][i]
for i in range(n):
    dp[i][0] = mat[i][0]


for i in range(1, n):
    for j in range(1, m):
        if mat[i][j] == 0:
            continue
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(max(map(max, dp)) ** 2)
