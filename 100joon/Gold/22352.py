import sys
from collections import deque

n, m = map(int, input().split())

before = []
after = []

for i in range(n):
    before.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    after.append(list(map(int, sys.stdin.readline().split())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = {}


def bfs(x, y, before_value, after_value):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[(x, y)] = 1
        before[x][y] = after_value
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited:
                if before[nx][ny] == before_value:
                    queue.append((nx, ny))


def check(before, after):
    flag = 0
    for i in range(n):
        for j in range(m):
            if before[i][j] != after[i][j] and (i, j) not in visited:
                if flag == 0:
                    bfs(i, j, before[i][j], after[i][j])
                    flag = 1
                else:
                    return


check(before, after)


for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            print("NO")
            sys.exit()
print("YES")
