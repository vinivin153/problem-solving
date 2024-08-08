import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(a, b):
    global max_value
    queue = deque()
    queue.append((a, b))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    max_value = max(max_value, cnt)


visited = [[False] * m for _ in range(n)]
pic = 0
max_value = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            pic += 1
            bfs(i, j)

print(pic)
print(max_value)
