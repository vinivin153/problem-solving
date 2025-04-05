import sys
from collections import deque
from itertools import combinations

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


vir = []
total = 0
for i in range(n):
    for j in range(n):
        if mat[i][j] == 2:
            vir.append((i, j))

        if mat[i][j] != 1:
            total += 1


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = sys.maxsize
for c in combinations(vir, m):
    time = -1
    visited = set()
    queue = deque()
    for r, c in c:
        visited.add((r, c))
        queue.append((r, c, 0))
    while queue:
        x, y, cnt = queue.popleft()
        time = cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] != 1 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append([nx, ny, cnt + 1])
    if len(visited) == total:
        ans = min(ans, time)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
