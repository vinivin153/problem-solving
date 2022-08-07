import sys
from collections import deque

n = int(input())
mat = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(rain, x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] > rain and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1


max_val = 0
for _ in range(n):
    k = list(map(int, input().split()))
    max_val = max(max_val, max(k))
    mat.append(k)

res = 1
for k in range(1, max_val):
    visited = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and mat[i][j] > k:
                visited[i][j] = 1
                bfs(k, i, j)
                cnt += 1
    res = max(res, cnt)

print(res)
