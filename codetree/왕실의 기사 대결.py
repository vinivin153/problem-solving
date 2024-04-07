# L: 체스판 크기, N: 기사 수, Q: 명령 수
# d 방향 정보: 0,1,2,3 -> 상 우 하 좌 ( 시계 방향 )

L, N, Q = map(int, input().split())

# 체스판 정보
mat = [[2] * (L + 2)]
for _ in range(L):
    mat.append([2] + list(map(int, input().split())) + [2])
mat.append([2] * (L + 2))


# 기사 정보
knights = {kn: set() for kn in range(1, N + 1)}

# 체력 정보
life = [0] * (N + 1)


for i in range(1, N + 1):
    r, c, h, w, k = map(int, input().split())
    life[i] = k

    for hh in range(h):
        for ww in range(w):
            knights[i].add((r + hh, c + ww))


# 데미지 정보
damage = [0] * (N + 1)

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def count_trap(kn):
    for x, y in knights[kn]:
        if mat[x][y] == 1:
            damage[kn] += 1


def move_knight(kn, direction, ordered):
    new_pos = set()
    for x, y in knights[kn]:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 이동하려는 곳이 벽인 경우
        if mat[nx][ny] == 2:
            return True
        new_pos.add((nx, ny))

    for num, pos in knights.items():
        # 이동하려는 곳에 다른 기사가 있는 경우
        if num != kn and new_pos & pos:
            if move_knight(num, direction, ordered):
                return True

    # 기사가 없는 경우 -> 이동가능
    can_move.append(kn)
    return False


def kill_knight():
    for kn in range(1, N + 1):
        if kn in knights and damage[kn] >= life[kn]:
            del knights[kn]


# 명령 정보
for q in range(Q):
    i, d = map(int, input().split())
    can_move = []
    # i 번째 기사가 체스판에 있는지 확인하기
    if i in knights and not move_knight(i, d, i):
        # 이동시키기
        for kn in can_move:
            new_set = {(x + dx[d], y + dy[d]) for x, y in knights[kn]}
            knights[kn] = new_set

            if kn != i:
                count_trap(kn)
        kill_knight()

ans = 0
for i in knights:
    ans += damage[i]

print(ans)
