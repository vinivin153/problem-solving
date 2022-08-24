import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

res = 0


def bfs(x, y, cnt):
    global res
    visited = set()
    visited.add((x, y))
    queue = deque()
    queue.append((x, y, cnt))
    tmp = 0
    while queue:
        x, y, cnt = queue.popleft()
        tmp = cnt
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == "L" and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, cnt + 1))
    if tmp > res:
        res = tmp


for i in range(n):
    for j in range(m):
        if mat[i][j] == "L":
            bfs(i, j, 0)

print(res)
