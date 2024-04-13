n, m, p, c, d = map(int, input().split())
rx, ry = map(int, input().split())
santa = {}
for _ in range(p):
    snum, sx, sy = map(int, input().split())
    santa[(sx, sy)] = snum

score = [0] * (p + 1)
stun = [0] * (p + 1)

# 상우하좌 + 대각선4개
dx = [-1, 0, 1, 0, -1, -1, 1, 1]
dy = [0, 1, 0, -1, -1, 1, -1, 1]


def valid_scope(x, y):
    return 1 <= x <= n and 1 <= y <= n


def calc_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def near_santa():
    # 가장 가까운 산타 찾기
    min_dist = 2500
    min_pos = (-1, -1)
    for pos in santa.keys():
        x, y = pos
        dist = calc_dist(rx, ry, x, y)
        # 더 가까운 경우
        if dist < min_dist:
            min_dist = dist
            min_pos = pos
        # 거리가 같은 경우
        elif dist == min_dist:
            # x가 큰 경우
            if min_pos[0] < x:
                min_dist = dist
                min_pos = pos
            # x가 같은 경우
            elif min_pos[0] == x:
                # y가 큰 경우
                if min_pos[1] < y:
                    min_dist = dist
                    min_pos = pos

    return min_pos


def crash(pos, direct, hitter):
    # 산타가 움직였을 땐 direct방향을 반대로 해서 넘겨주어야함
    # crash 전에 산타나 루돌프의 좌표를 업데이트
    # pos는 산타좌표
    x, y = pos
    nx, ny = (99, 99)
    if hitter == "rudol":
        nx = x + dx[direct] * c
        ny = y + dy[direct] * c
    elif hitter == "santa":
        nx = x + dx[direct] * d
        ny = y + dy[direct] * d

    if not valid_scope(nx, ny):
        # 기존의 산타 위치 삭제
        del santa[pos]
    # 범위 벗어나지 않으면 기절 및 상호작용 체크
    else:
        pre_num = santa[pos]
        stun[pre_num] = 2

        # 기존의 산타 위치 삭제
        del santa[pos]

        # 현재 nx ny는 날아간 좌표
        stack = [(nx, ny)]
        while stack:
            xx, yy = stack.pop()
            if not valid_scope(xx, yy):
                break

            # 이동한 곳에 다른 산타 있는 경우
            if (xx, yy) in santa:
                # 원래 자리에 있던 산타번호 저장
                temp = santa[(xx, yy)]
                santa[(xx, yy)] = pre_num
                pre_num = temp
                stack.append((xx + dx[direct], yy + dy[direct]))
            else:
                santa[(xx, yy)] = pre_num


def move_r():
    global rx, ry

    x, y = near_santa()
    min_dist = 2500
    min_pos = (99, 99)
    direct = -1
    for i in range(8):
        nx = rx + dx[i]
        ny = ry + dy[i]
        if valid_scope(nx, ny):
            dist = calc_dist(nx, ny, x, y)
            if dist < min_dist:
                min_dist = dist
                min_pos = (nx, ny)
                direct = i

    # 루돌프 위치 업데이트
    rx, ry = min_pos
    # 산타와 충돌하는 경우
    if min_dist == 0:
        score[santa[min_pos]] += c
        crash(min_pos, direct, "rudol")


def move_s():
    for num in range(1, p + 1):
        pos = (-1, -1)
        if num in santa.values():
            pos = [pp for pp, nn in santa.items() if nn == num][0]
        # 스턴이 아닌 경우에 이동가능
        if stun[num] > 0:
            continue
        x, y = pos

        min_dist = calc_dist(x, y, rx, ry)
        min_pos = (x, y)
        direct = -1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 유효한 범위 및 다른산타가 있는 경우
            if valid_scope(nx, ny) and (nx, ny) not in santa:
                dist = calc_dist(nx, ny, rx, ry)
                if dist < min_dist:
                    min_dist = dist
                    min_pos = (nx, ny)
                    direct = i

        # 이동한 경우 좌표 업데이트
        if pos != min_pos:
            # 새로운 위치에 산타 생성 및 기존 산타위치 제거
            santa[min_pos] = santa[pos]
            del santa[pos]
            # 산타가 루돌프와 충돌하는 경우
            if min_pos == (rx, ry):
                score[santa[min_pos]] += d
                crash(min_pos, (direct + 2) % 4, "santa")


for k in range(m):
    if not santa:
        break

    for i in range(1, p + 1):
        if stun[i] > 0:
            stun[i] -= 1

    move_r()
    move_s()

    for num in santa.values():
        score[num] += 1

print(*score[1:])
