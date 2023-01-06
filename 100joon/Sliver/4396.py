import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

mat = [list(input().rstrip()) for _ in range(n)]
ans = [list(input().rstrip()) for _ in range(n)]

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

flag = 0


def bfs(x, y):
    global flag
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        cnt = 0
        if mat[x][y] == "*":
            flag = 1
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] == "*":
                    cnt += 1
                if ans[nx][ny] == "x":
                    queue.append((nx, ny))
        ans[x][y] = cnt


for i in range(n):
    for j in range(n):
        if ans[i][j] == "x":
            bfs(i, j)

if flag:
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "*":
                print("*", end="")
            else:
                print(ans[i][j], end="")
        print()
else:
    for i in range(n):
        for j in range(n):
            print(ans[i][j], end="")
        print()
