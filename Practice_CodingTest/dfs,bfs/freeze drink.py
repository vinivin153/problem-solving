# dfs 반복

import sys

n, m = map(int, input().split())

icetray = []
for i in range(n):
    icetray.append(list(sys.stdin.readline().rstrip()))


visited = {}
stack = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(value: list):
    stack.append(value)
    while stack:
        x, y = stack.pop()
        visited[(x, y)] = 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if (
                0 <= nx < n
                and 0 <= ny < m
                and icetray[nx][ny] == "0"
                and (nx, ny) not in visited
            ):
                stack.append((nx, ny))


cnt = 0
for i in range(n):
    for j in range(m):
        if icetray[i][j] == "0" and (i, j) not in visited:
            dfs((i, j))
            cnt += 1

print(cnt)
