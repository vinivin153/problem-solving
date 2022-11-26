# 모래섬
# 0 - 물 1 - 모래
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited.add((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 0:
                    sink.add((x, y))
                elif (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))


cnt = 0
island = 0
while True:
    island = 0
    visited = set()
    sink = set()
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 1 and (i, j) not in visited:
                island += 1
                bfs(i, j)

    for x, y in sink:
        mat[x][y] = 0

    if island == 0:
        cnt = -1
        break

    if island > 1:
        break

    cnt += 1

print(cnt)
