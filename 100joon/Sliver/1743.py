import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
mat = [[False] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    mat[x - 1][y - 1] = True


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0


def bfs(x, y):
    global ans
    queue = deque()
    queue.append([x, y])
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny]:
                    queue.append([nx, ny])
                    cnt += 1
                    mat[nx][ny] = False

    if cnt > ans:
        ans = cnt


for i in range(n):
    for j in range(m):
        if mat[i][j]:
            mat[i][j] = False
            bfs(i, j)


print(ans)
