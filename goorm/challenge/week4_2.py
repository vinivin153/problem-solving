# 단풍나무
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
new_mat = [mat[i][:] for i in range(n)]
ans = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs():
    global ans
    while queue:
        x, y, day = queue.popleft()
        if ans != day:
            mat = [new_mat[i][:] for i in range(n)]
        ans = day
        cnt = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] <= 0:
                    cnt += 1
        new_mat[x][y] -= cnt
        if new_mat[x][y] > 0:
            queue.append((x, y, day + 1))


queue = deque()
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            queue.append((i, j, 1))

bfs()
print(ans)
