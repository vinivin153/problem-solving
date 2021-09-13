import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

maze = [list(map(int, input().rstrip())) for _ in range(n)]

visited = set()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    visited.add((0, 0))
    while queue:
        x, y, cnt = queue.popleft()
        if x == n - 1 and y == m - 1:
            return cnt
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in visited and maze[nx][ny] == 1:
                    queue.append((nx, ny, cnt + 1))
                    visited.add((nx, ny))


print(bfs())
