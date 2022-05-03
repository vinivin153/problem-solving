import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

dp[0][0] = mat[0][0]

dx = [0, -1, -1]
dy = [-1, 0, -1]

for i in range(n):
    for j in range(m):
        for k in range(3):
            nx = dx[k] + i
            ny = dy[k] + j
            if 0 <= nx < n and 0 <= ny < m:
                dp[i][j] = max(dp[i][j], dp[nx][ny] + mat[i][j])

print(dp[n - 1][m - 1])
