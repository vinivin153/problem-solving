import sys
from collections import deque

input = sys.stdin.readline


def bfs(x1, y1, x2, y2, l):
    queue = deque()
    queue.append((x1, y1, 0))
    visited[x1][y1] = 1
    while queue:
        x1, y1, cnt = queue.popleft()
        if x1 == x2 and y1 == y2:
            print(cnt)
            break
        for i in range(8):
            nx = dx[i] + x1
            ny = dy[i] + y1
            if 0 <= nx < l and 0 <= ny < l:
                if visited[nx][ny] == 0:
                    queue.append((nx, ny, cnt + 1))
                    visited[nx][ny] = 1


dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

t = int(input())
for _ in range(t):
    l = int(input())
    visited = [[0 for _ in range(l)] for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    bfs(x1, y1, x2, y2, l)
