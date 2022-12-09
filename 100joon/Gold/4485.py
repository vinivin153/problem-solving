import sys
from heapq import *

input = sys.stdin.readline
cnt = 1
n = int(input())
while n:
    cave = [list(map(int, input().split())) for _ in range(n)]
    dist = [[sys.maxsize] * n for _ in range(n)]
    dist[0][0] = cave[0][0]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    ans = []
    heap = []
    heappush(heap, [dist[0][0], [0, 0]])
    while heap:
        c, [x, y] = heappop(heap)

        if x == n - 1 and y == n - 1:
            continue

        if c > dist[x][y]:
            continue

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < n:
                if dist[nx][ny] > c + cave[nx][ny]:
                    dist[nx][ny] = c + cave[nx][ny]
                    heappush(heap, [c + cave[nx][ny], [nx, ny]])

    print(f"Problem {cnt}: {dist[n-1][n-1]}")
    cnt += 1
    n = int(input())
