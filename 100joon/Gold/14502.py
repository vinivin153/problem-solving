import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

res = 0


def backtracking(cnt, i, j):
    global res
    if cnt == 3:
        new_mat = [mat[i][:] for i in range(n)]
        for x in range(n):
            for y in range(m):
                if new_mat[x][y] == 2:
                    bfs(new_mat, x, y)
        sum1 = 0
        for k in new_mat:
            sum1 += k.count(0)
        if sum1 > res:
            res = sum1
        return

    for x in range(i, n):
        for y in range(j, m):
            if mat[x][y] == 0:
                mat[x][y] = 1
                backtracking(cnt + 1, x, y + 1)
                mat[x][y] = 0
        j = 0


queue = deque()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(new_mat, x, y):
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if new_mat[nx][ny] == 0:
                    new_mat[nx][ny] = 3
                    queue.append((nx, ny))


backtracking(0, 0, 0)
print(res)
