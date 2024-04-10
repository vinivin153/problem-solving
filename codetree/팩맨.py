from collections import defaultdict

m, t = map(int, input().split())
pacman = list(map(int, input().split()))
monsters = [list(map(int, input().split())) for _ in range(m)]
dead = [[0] * 5 for _ in range(5)]
eggs = []

d = {
    1: (-1, 0),
    2: (-1, -1),
    3: (0, -1),
    4: (1, -1),
    5: (1, 0),
    6: (1, 1),
    7: (0, 1),
    8: (-1, 1),
}


def valid_scope(x, y):
    if 1 <= x <= 4 and 1 <= y <= 4:
        return True
    else:
        return False


def move_monster():
    for k in range(len(monsters)):
        x, y, z = monsters[k]
        for i in range(8):
            idx = ((z + i - 1) % 8) + 1
            nx = x + d[idx][0]
            ny = y + d[idx][1]
            # 벗어나지 않고, 죽은 시체 없고, 팩맨 위치가 아닌지
            if valid_scope(nx, ny) and dead[nx][ny] == 0 and [nx, ny] != pacman:

                monsters[k] = [nx, ny, idx]
                break


def move_pacman():
    global pacman
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    max_eat = -1
    pos1 = [0, 0]
    pos2 = [0, 0]
    pos3 = [0, 0]

    count_monster = defaultdict(int)
    for x, y, z in monsters:
        count_monster[(x, y)] += 1

    x, y = pacman
    for i in range(4):
        for j in range(4):
            for k in range(4):
                px1, py1 = x + dx[i], y + dy[i]
                px2, py2 = px1 + dx[j], py1 + dy[j]
                px3, py3 = px2 + dx[k], py2 + dy[k]

                if (
                    valid_scope(px1, py1)
                    and valid_scope(px2, py2)
                    and valid_scope(px3, py3)
                ):
                    sum_eat = (
                        count_monster[(px1, py1)]
                        + count_monster[(px2, py2)]
                        + count_monster[(px3, py3)]
                    )
                    if px1 == px3 and py1 == py3:
                        sum_eat -= count_monster[(px3, py3)]
                    if sum_eat > max_eat:
                        pos1 = [px1, py1]
                        pos2 = [px2, py2]
                        pos3 = [px3, py3]
                        max_eat = sum_eat

    pacman = pos3
    new_monster = []
    for x, y, z in monsters:
        if [x, y] not in [pos1, pos2, pos3]:
            new_monster.append([x, y, z])
        else:
            dead[x][y] = 3

    return new_monster


def disappear():
    for i in range(1, 5):
        for j in range(1, 5):
            if dead[i][j] > 0:
                dead[i][j] -= 1


for _ in range(t):
    # 복제
    eggs = monsters[:]
    move_monster()
    monsters = move_pacman()
    disappear()
    monsters += eggs

print(len(monsters))
