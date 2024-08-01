import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

mat = [list(map(int, input().split())) for _ in range(n)]
shark_size = 2
curr_x, curr_y = 0, 0
time = 0
eat_fish = 0


def find_current_loc():
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 9:
                mat[i][j] = 0
                return [i, j]


dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def find_fish():
    global curr_x, curr_y, time, shark_size, eat_fish
    queue = deque()

    queue.append((curr_x, curr_y, 0))
    visited = set()
    min_dist = 400
    min_pos = [n, n]
    while queue:
        x, y, cnt = queue.popleft()
        if min_dist < cnt:
            break
        # 먹이 찾기
        if 0 < mat[x][y] < shark_size:
            # 더 위에 있거나 같은 높이에서 왼쪽에 있는 경우
            if min_dist == cnt:
                if x < min_pos[0] or (x == min_pos[0] and y < min_pos[1]):
                    min_dist = cnt
                    min_pos = [x, y]
            else:
                min_dist = cnt
                min_pos = [x, y]
            continue

        # 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 방문하지 않는 곳과 사이즈보다 작거나 같은 물고기
                if (nx, ny) not in visited and mat[nx][ny] <= shark_size:
                    visited.add((nx, ny))
                    queue.append((nx, ny, cnt + 1))

    if min_dist == 400:
        return False

    time += min_dist
    mat[min_pos[0]][min_pos[1]] = 0
    curr_x, curr_y = min_pos
    eat_fish += 1

    if eat_fish == shark_size:
        shark_size += 1
        eat_fish = 0

    return True


curr_x, curr_y = find_current_loc()
while True:
    if not find_fish():
        break
print(time)
