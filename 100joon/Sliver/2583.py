import sys
from collections import deque


input = sys.stdin.readline

n, m, k = map(int, input().split())
mat = [[0 for _ in range(m)] for _ in range(n)]
res = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    cnt = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 0:
                    mat[nx][ny] = -1
                    queue.append((nx, ny))
                    cnt += 1
    res.append(cnt)


for i in range(k):
    y1, x2, y2, x1 = map(int, input().split())

    for i in range(n - x1, n - x2):
        for j in range(y1, y2):
            mat[i][j] = 1

for i in range(n):
    for j in range(m):
        if mat[i][j] == 0:
            mat[i][j] = -1
            bfs(i, j)

res.sort()
print(len(res))
print(*res)
