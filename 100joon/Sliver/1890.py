import sys

input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1


for i in range(n):
    for j in range(n):

        for x in range(i):
            if mat[x][j] == i - x:
                dp[i][j] += dp[x][j]

        for y in range(j):
            if mat[i][y] == j - y:
                dp[i][j] += dp[i][y]


print(dp[n - 1][n - 1])
