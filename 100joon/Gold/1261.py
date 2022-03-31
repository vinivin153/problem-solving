# 다른 방법으로 풀어보기
import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

mat = []

for _ in range(n):
    mat.append(list(map(int, input().rstrip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[10000 for _ in range(m)] for _ in range(n)]
ans = []


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            ans.append(visited[x][y])
            continue
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if mat[nx][ny] == 0 and visited[nx][ny] > visited[x][y]:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y]
                elif mat[nx][ny] == 1 and visited[nx][ny] > visited[x][y] + 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1


bfs()
print(min(ans))
