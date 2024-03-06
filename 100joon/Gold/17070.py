import sys

input = sys.stdin.readline
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]


# 왼쪽 위 대각선
dx = [0, -1, -1]
dy = [-1, 0, -1]


for i in range(1, n):
    if mat[0][i] == 0:
        dp[0][i][0] = 1
    else:
        break


for x in range(1, n):
    for y in range(2, n):
        for k in range(3):
            nx = x + dx[k]
            ny = y + dy[k]
            if k == 0 and mat[x][y] == 0:
                # 왼쪽 -> 대각 왼쪽 가능
                dp[x][y][k] = dp[nx][ny][0] + dp[nx][ny][2]
            elif k == 1 and mat[x][y] == 0:
                # 위 -> 위, 대각 가능
                dp[x][y][k] = dp[nx][ny][1] + dp[nx][ny][2]
            else:
                if mat[x][y] == 0 and mat[x][y - 1] == 0 and mat[x - 1][y] == 0:
                    # 대각선 ->
                    dp[x][y][k] = sum(dp[nx][ny])

print(sum(dp[n - 1][n - 1]))
