import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]
visited = set()
visited.add((x1 - 1, y1 - 1))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

queue = deque()
queue.append((x1 - 1, y1 - 1, 1))
while queue:
    x, y, cnt = queue.popleft()

    if mat[x][y] == "#":
        print(cnt)
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if (nx, ny) not in visited:
                if mat[nx][ny] == "1":
                    queue.append((nx, ny, cnt + 1))
                else:
                    queue.appendleft((nx, ny, cnt))
            visited.add((nx, ny))
