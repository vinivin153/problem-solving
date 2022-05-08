import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    while queue:
        x, y, check = queue.popleft()
        if x == n - 1 and y == m - 1:
            print(visited[x][y][check])
            return
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny][check] == 0:
                    if mat[nx][ny] == 1 and check == 0:
                        visited[nx][ny][1] = visited[x][y][check] + 1
                        queue.append((nx, ny, 1))
                    elif mat[nx][ny] == 0:
                        visited[nx][ny][check] = visited[x][y][check] + 1
                        queue.append((nx, ny, check))

    print(-1)
    return


bfs()
