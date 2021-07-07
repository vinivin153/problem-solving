import sys
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, 1))
    while queue:
        x, y, cnt = queue.popleft()
        visited[(x, y)] = cnt
        if x == n - 1 and y == m - 1:
            return cnt
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited and maze[nx][ny] == "1":
                    queue.append((nx, ny, cnt + 1))


n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(sys.stdin.readline().rstrip()))

visited = {}


print(bfs(0, 0))
