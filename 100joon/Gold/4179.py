import sys
from collections import deque

input = sys.stdin.readline

row, col = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(row)]

fire = set()
escape = set()
current = (0, 0)
visited = set()

for r in range(row):
    for c in range(col):
        if mat[r][c] == "J":
            current = (r, c)
        elif mat[r][c] == "F":
            fire.add((r, c))

new_fire = fire

for i in range(col):
    if mat[0][i] in (".", "J"):
        escape.add((0, i))

    if mat[row - 1][i] in (".", "J"):
        escape.add((row - 1, i))

for i in range(row):
    if mat[i][0] in (".", "J"):
        escape.add((i, 0))

    if mat[i][col - 1] in (".", "J"):
        escape.add((i, col - 1))


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

pre = 0
queue = deque()
queue.append((current, 1))
while queue:
    loc, time = queue.popleft()
    x, y = loc

    if pre != time:
        pre = time
        temp = set()
        for xx, yy in new_fire:
            for i in range(4):
                nx = xx + dx[i]
                ny = yy + dy[i]
                if 0 <= nx < row and 0 <= ny < col:
                    if (nx, ny) not in fire and mat[nx][ny] != "#":
                        temp.add((nx, ny))
        new_fire = temp
        fire = fire.union(new_fire)

    if loc in escape:
        print(time)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < row and 0 <= ny < col:
            if mat[nx][ny] == "." and (nx, ny) not in visited and (nx, ny) not in fire:
                queue.append(((nx, ny), time + 1))
                visited.add((nx, ny))
else:
    print("IMPOSSIBLE")
