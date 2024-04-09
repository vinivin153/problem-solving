from collections import deque


n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
basecamp = []

# 베이스 캠프 위치 저장
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            basecamp.append((i, j))


onBoard = deque()  # 격자 위에 있는 사람 리스트


# 편의점 리스트
conven = []
for _ in range(m):
    a, b = map(int, input().split())
    conven.append((a - 1, b - 1))

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def valid_scope(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    else:
        return False


def calc_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def short_dist(x1, y1, conven_pos):
    visited = set()
    visited.add((x1, y1))
    queue = deque()
    queue.append((x1, y1, 0))
    while queue:
        x, y, cnt = queue.popleft()

        if (x, y) == conven_pos:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 방문하지 않은 곳, 유효 범위, 빈칸(0) or 선택되지 않은 베이스캠프(1)
            if (nx, ny) not in visited and valid_scope(nx, ny) and mat[nx][ny] >= 0:
                visited.add((nx, ny))
                queue.append((nx, ny, cnt + 1))

    return -1


# 가까운 basecamp선정
def select_basecamp(conven_pos):
    min_dist = 10**5
    min_pos = (-1, -1)
    for bx, by in basecamp:
        dist = short_dist(bx, by, conven_pos)

        # 기존 거리보다 가까운 경우
        if dist != -1 and dist < min_dist:
            min_dist = dist
            min_pos = (bx, by)

    basecamp.remove(min_pos)
    mat[min_pos[0]][min_pos[1]] = -1
    onBoard.append([min_pos, conven_pos])


# 보드위에 있는 사람들 이동
def move(onBoard):
    global finish
    new_onBoard = []
    cant_move = []
    while onBoard:
        curr_pos, conven_pos = onBoard.popleft()
        x, y = curr_pos
        min_dist = 10**5
        min_pos = (-1, -1)

        # 상하좌우 중 가장 최단거리 찾기
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 유효 범위 & 빈칸(0) or 선택되지 않은 베이스캠프(1)
            if valid_scope(nx, ny) and mat[nx][ny] >= 0:
                dist = short_dist(nx, ny, conven_pos)
                if dist != -1 and dist < min_dist:
                    min_dist = dist
                    min_pos = (nx, ny)

        # 편의점 도착한 경우
        if min_pos == conven_pos:
            finish -= 1
            cant_move.append(min_pos)
        # 단순 이동인 경우
        else:
            new_onBoard.append([min_pos, conven_pos])

    # 도착 후 모든 사람의 이동이 끝난 후 이동하지 못하게 막기
    for x, y in cant_move:
        mat[x][y] = -1

    return new_onBoard


finish = m  # 도착한 사람들 정보
time = 0  # 걸린 시간

while finish:
    time += 1

    # 사람들 이동
    newBoard = move(onBoard)
    onBoard = deque(newBoard)

    # m번째 사람 베이스 캠프 선택하기
    if time <= m:
        select_basecamp(conven[time - 1])


print(time)
