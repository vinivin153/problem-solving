import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

MAX = 100 * 1000
visited = [[[0] * 3 for _ in range(m)] for _ in range(n + 1)]
for i in range(1, n + 1):
    visited[i][0][2], visited[i][m - 1][0] = MAX, MAX

for i in range(1, n + 1):
    for j in range(m):
        if j + 1 < m:
            visited[i][j][0] = (
                min(visited[i - 1][j + 1][1], visited[i - 1][j + 1][2]) + mat[i - 1][j]
            )
        if 0 <= j - 1:
            visited[i][j][2] = (
                min(visited[i - 1][j - 1][0], visited[i - 1][j - 1][1]) + mat[i - 1][j]
            )

        visited[i][j][1] = (
            min(visited[i - 1][j][0], visited[i - 1][j][2]) + mat[i - 1][j]
        )

print(min(min(row) for row in visited[n]))
