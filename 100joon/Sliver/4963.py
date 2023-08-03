import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, -1, 0, 1, -1, 0, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and mat[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True


while True:
    c, r = map(int, input().split())
    if c == 0 and r == 0:
        break
    visited = [[False] * c for _ in range(r)]
    mat = [list(map(int, input().split())) for _ in range(r)]

    cnt = 0
    for i in range(r):
        for j in range(c):
            if mat[i][j] and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                bfs(i, j)
    print(cnt)
