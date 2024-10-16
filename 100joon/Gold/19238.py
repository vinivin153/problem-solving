import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x1, y1, fin_x, fin_y):
    queue = deque()
    queue.append((x1, y1, 0))
    visited = set()
    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == (fin_x, fin_y):
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, cnt + 1))

    return -1


def find_near_person():
    near_dist = 400
    near_idx = -1
    r, c = 100, 100
    queue = deque()
    queue.append((taxi_x, taxi_y, 0))
    visited = set()
    visited.add((taxi_x, taxi_y))

    while queue:
        x, y, cnt = queue.popleft()
        v = mat2[x][y]
        if mat2[x][y] >= 0:
            if cnt < near_dist:
                near_dist = cnt
                near_idx = v
                r, c = pickup_pos[v][0], pickup_pos[v][1]
            elif cnt == near_dist:
                if pickup_pos[v][0] < r:
                    near_dist = cnt
                    near_idx = v
                    r, c = pickup_pos[v][0], pickup_pos[v][1]
                elif pickup_pos[v][0] == r:
                    if pickup_pos[v][1] < c:
                        near_dist = cnt
                        near_idx = v
                        r, c = pickup_pos[v][0], pickup_pos[v][1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if mat[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, cnt + 1))

    return near_dist, near_idx


n, m, feul = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
mat2 = [[-1] * n for _ in range(n)]
a, b = map(int, input().split())
taxi_x, taxi_y = a - 1, b - 1

dist = [0] * m
pickup_pos = {}

# 출발지 - 도착지 최단경로 구하기
for i in range(m):
    start_x, start_y, fin_x, fin_y = map(int, input().split())
    pickup_pos[i] = (start_x - 1, start_y - 1, fin_x - 1, fin_y - 1)
    d = bfs(*pickup_pos[i])
    mat2[start_x - 1][start_y - 1] = i

    # if d == -1:
    #     print(-1)
    #     sys.exit()

    dist[i] = d

for i in dist:
    if i == -1:
        print(-1)
        sys.exit()


for i in range(m):
    near_dist, near_idx = find_near_person()
    if near_idx == -1:
        print(-1)
        break

    feul -= near_dist + dist[near_idx]
    # print(near_idx, near_dist, "near_dist")
    if feul < 0:
        print(-1)
        break

    mat2[pickup_pos[near_idx][0]][pickup_pos[near_idx][1]] = -1
    feul += dist[near_idx] * 2
    taxi_x, taxi_y = pickup_pos[near_idx][2], pickup_pos[near_idx][3]
    del pickup_pos[near_idx]

    # print("feul")

else:
    print(feul)
