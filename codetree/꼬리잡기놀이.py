n, m, k = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

BLANK = 0
HEAD = 1
NORMAL = 2
TAIL = 3
LINE = 4

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

teams = {}
score = 0


def valid_scope(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(r, c, tn):
    stack = [(r, c)]
    teams[tn] = [(r, c)]
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if valid_scope(nx, ny) and (nx, ny) not in teams[tn]:
                if (
                    (mat[x][y] == HEAD and mat[nx][ny] == NORMAL)
                    or mat[x][y] == NORMAL
                    and mat[nx][ny] in (NORMAL, TAIL)
                ):
                    teams[tn].append((nx, ny))
                    stack.append((nx, ny))
                    break


def find_team():
    team_num = 1
    for i in range(n):
        for j in range(n):
            if mat[i][j] == HEAD:
                dfs(i, j, team_num)
                team_num += 1


def move():
    for tn, team in teams.items():
        new_head = (-1, -1)
        for i in range(4):
            x, y = team[0]
            nx = x + dx[i]
            ny = y + dy[i]

            if valid_scope(nx, ny) and mat[nx][ny] in (LINE, TAIL):
                new_head = (nx, ny)
                break

        x, y = team.pop()
        mat[x][y] = LINE
        teams[tn] = [new_head] + team[:]

        for x, y in teams[tn]:
            mat[x][y] = NORMAL
        x, y = teams[tn][0]
        mat[x][y] = HEAD
        x, y = teams[tn][-1]
        mat[x][y] = TAIL


def hit(x, y):
    global score

    for tn, team in teams.items():
        if (x, y) in team:
            # 점수
            score += (team.index((x, y)) + 1) ** 2

            # 머리와 꼬리 변경
            x1, y1 = team[0]
            x2, y2 = team[-1]
            mat[x1][y1], mat[x2][y2] = mat[x2][y2], mat[x1][y1]
            teams[tn].reverse()

            return True

    return False


def shoot(round):
    if 0 <= round < n:
        for c in range(n):
            if hit(round, c):
                break

    elif n <= round < 2 * n:
        for r in range(n - 1, -1, -1):
            if hit(r, round - n):
                break

    elif 2 * n <= round < 3 * n:
        for c in range(n - 1, -1, -1):
            if hit(n - (round - 2 * n) - 1, c):
                break

    elif 3 * n <= round < 4 * n:
        for r in range(n):
            if hit(r, n - (round - 3 * n) - 1):
                break


find_team()
for rr in range(k):
    move()
    shoot(rr % (4 * n))

print(score)
