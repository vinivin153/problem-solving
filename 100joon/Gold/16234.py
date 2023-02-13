import sys
from collections import deque

input = sys.stdin.readline

n, l, r = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x, y):
    global visited
    queue = deque()
    queue.append([x, y])
    visited[x][y] = True
    loc = []
    total = 0
    while queue:
        x, y = queue.popleft()
        total += mat[x][y]
        loc.append([x, y])
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny] and l <= abs(mat[x][y] - mat[nx][ny]) <= r:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
    if len(loc) > 1:
        value = total // len(loc)
        return [loc, value]


ans = 0
while True:
    move = []
    visited = [[False] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                res = dfs(x, y)
                if res:
                    move.append(res)

    if move:
        for loc, value in move:
            for x, y in loc:
                mat[x][y] = value
        ans += 1
    else:
        print(ans)
        break
