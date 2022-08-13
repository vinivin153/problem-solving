import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 1:
                    mat[nx][ny] = -1
                    queue.append((nx, ny))


input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())

    mat = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        y, x = map(int, input().split())
        mat[x][y] = 1

    res = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1:
                mat[i][j] = -1
                res += 1
                bfs(i, j)
    print(res)
