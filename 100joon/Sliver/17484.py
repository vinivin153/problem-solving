import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

min_cost = 10 ** 8

dy = [-1, 0, 1]


def bfs(i):
    global min_cost
    queue = deque()
    queue.append((0, i, mat[0][i], -1))
    while queue:
        x, y, cost, pre = queue.popleft()
        if x == n - 1:
            if min_cost > cost:
                min_cost = cost
            continue

        for i in range(3):
            ny = y + dy[i]
            if 0 <= ny < m and pre != i:
                if cost + mat[x + 1][ny] < min_cost:
                    queue.append((x + 1, ny, cost + mat[x + 1][ny], i))


for i in range(m):
    bfs(i)

print(min_cost)
