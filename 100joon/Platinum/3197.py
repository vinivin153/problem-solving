import sys
from collections import deque


input = sys.stdin.readline
r, c = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

L = []
next = deque()


def divide_sector(x, y, s):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()

        if mat[x][y] == "L":
            L.append(sector)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                if mat[nx][ny] == "X":
                    visited[nx][ny] = s
                    next.append((nx, ny))
                else:
                    visited[nx][ny] = s
                    queue.append((nx, ny))


def find_parent(x):
    if link[x] == x:
        return x
    link[x] = find_parent(link[x])
    return link[x]


sector = 1
for i in range(r):
    for j in range(c):
        if not visited[i][j] and mat[i][j] != "X":
            visited[i][j] = sector
            divide_sector(i, j, sector)
            sector += 1

L1, L2 = L
link = [0] * sector
for i in range(1, sector):
    link[i] = i

cnt = 0
while find_parent(link[L1]) != find_parent(link[L2]):
    temp = deque()
    while next:
        x, y = next.popleft()
        mat[x][y] = "."

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < r
                and 0 <= ny < c
                and link[visited[x][y]] != link[visited[nx][ny]]
            ):
                if mat[nx][ny] == "X":
                    visited[nx][ny] = visited[x][y]
                    temp.append((nx, ny))
                else:
                    a = find_parent(visited[nx][ny])
                    b = find_parent(visited[x][y])
                    if a > b:
                        link[a] = b
                    else:
                        link[b] = a

    next = temp
    cnt += 1
print(cnt)
