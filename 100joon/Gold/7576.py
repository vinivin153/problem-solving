import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())
box = []
for _ in range(n):
    box.append(list(map(int, input().split())))

queue = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append((i, j, 0))


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


day = 0
while queue:
    x, y, cnt = queue.popleft()
    day = cnt
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                queue.append((nx, ny, cnt + 1))
                box[nx][ny] = 1

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            sys.exit(0)

print(day)
