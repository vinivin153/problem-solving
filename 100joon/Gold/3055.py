import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

start = []
water = []


def vaild_scope(x, y):
    return 0 <= x < n and 0 <= y < m


def init():
    global start, water
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "S":
                start = (i, j)
            elif mat[i][j] == "*":
                water.append((i, j))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def overflow():
    next_water = []
    for x, y in water:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if vaild_scope(nx, ny):
                if mat[nx][ny] == ".":
                    next_water.append((nx, ny))
                    mat[nx][ny] = "*"

    return next_water


def move():
    global water
    queue = deque()
    queue.append((*start, 0))
    visited = set()
    visited.add(start)
    prev = -1
    while queue:
        x, y, cnt = queue.popleft()

        if mat[x][y] == "D":
            print(cnt)
            return

        if prev != cnt:
            water = overflow()
            prev = cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if vaild_scope(nx, ny) and (nx, ny) not in visited:
                if mat[nx][ny] in (".", "D"):
                    queue.append((nx, ny, cnt + 1))
                    visited.add((nx, ny))

    print("KAKTUS")


init()
move()
