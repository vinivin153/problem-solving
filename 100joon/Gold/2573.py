import sys
from collections import deque

iceberg = []
visited = {}


def bfs(m, n, iceberg):
    global visited
    change = []
    queue = deque()
    queue.append([m, n])

    while queue:
        a, b = queue.popleft()
        cnt_sea = 0
        if (a, b) not in visited:
            visited[a, b] = 1
            if iceberg[a + 1][b] <= 0:
                cnt_sea += 1
            else:
                queue.append([a + 1, b])

            if iceberg[a - 1][b] <= 0:
                cnt_sea += 1
            else:
                queue.append([a - 1, b])

            if iceberg[a][b + 1] <= 0:
                cnt_sea += 1
            else:
                queue.append([a, b + 1])

            if iceberg[a][b - 1] <= 0:
                cnt_sea += 1
            else:
                queue.append([a, b - 1])

            if cnt_sea:
                change.append([a, b, cnt_sea])

    return change


n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    iceberg.append(list(map(int, sys.stdin.readline().split())))


change = []
year = 0
while True:
    visited = {}
    cnt = 0
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if iceberg[i][j] > 0 and (i, j) not in visited:
                cnt += 1
                if cnt > 1:
                    print(year)
                    sys.exit(0)
                change = bfs(i, j, iceberg)
                for a, b, c in change:
                    iceberg[a][b] -= c

    year += 1
    if cnt == 0:
        print(0)
        break
