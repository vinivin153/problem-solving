import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]
recent = [[0] * m for _ in range(n)]


def pick_attacker():
    at_x = -1
    at_y = -1
    at_value = 5001
    for i in range(n):
        for j in range(m):
            if mat[i][j] != 0:
                if at_value > mat[i][j]:
                    at_x = i
                    at_y = j
                    at_value = mat[at_x][at_y]
                elif at_value == mat[i][j]:
                    if recent[at_x][at_y] < recent[i][j]:
                        at_x = i
                        at_y = j
                        at_value = mat[at_x][at_y]
                    elif recent[at_x][at_y] == recent[i][j]:
                        if (at_x + at_y) < (i + j):
                            at_x = i
                            at_y = j
                            at_value = mat[at_x][at_y]
                        elif (at_x + at_y) == (i + j):
                            if at_y < j:
                                at_x = i
                                at_y = j
                                at_value = mat[at_x][at_y]

    mat[at_x][at_y] += n + m
    return [at_x, at_y]


def pick_target(attacker):
    at_x, at_y = attacker
    tar_x = -1
    tar_y = -1
    tar_value = 0
    for i in range(n):
        for j in range(m):
            if [i, j] != [at_x, at_y] and mat[i][j] != 0:
                if tar_value < mat[i][j]:
                    tar_x = i
                    tar_y = j
                    tar_value = mat[tar_x][tar_y]
                elif tar_value == mat[i][j]:
                    if recent[tar_x][tar_y] > recent[i][j]:
                        tar_x = i
                        tar_y = j
                        tar_value = mat[tar_x][tar_y]
                    elif recent[tar_x][tar_y] == recent[i][j]:
                        if (tar_x + tar_y) > (i + j):
                            tar_x = i
                            tar_y = j
                            tar_value = mat[tar_x][tar_y]
                        elif (tar_x + tar_y) == (i + j):
                            if tar_y > j:
                                tar_x = i
                                tar_y = j
                                tar_value = mat[tar_x][tar_y]

    return [tar_x, tar_y]


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def attack(attacker, target):
    at_x, at_y = attacker
    atk = mat[at_x][at_y]
    atk2 = atk // 2
    tar_x, tar_y = target
    queue = deque()
    queue.append(attacker)
    attacked = [attacker, target]
    visited = [[[]] * m for _ in range(n)]

    while queue:
        x, y = queue.popleft()
        if x == tar_x and y == tar_y:
            mat[x][y] = max(mat[x][y] - atk, 0)
            while visited[x][y] != attacker:
                x, y = visited[x][y]
                attacked.append([x, y])
                mat[x][y] = max(mat[x][y] - atk2, 0)
            break
        for i in range(4):
            nx = (x + dx[i]) % n
            ny = (y + dy[i]) % m
            if mat[nx][ny] != 0 and not visited[nx][ny]:
                visited[nx][ny] = [x, y]
                queue.append([nx, ny])
    else:
        mat[tar_x][tar_y] = max(mat[tar_x][tar_y] - atk, 0)
        dx2 = [-1, -1, -1, 0, 0, 1, 1, 1]
        dy2 = [-1, 0, 1, -1, 1, -1, 0, 1]
        for i in range(8):
            nx = (tar_x + dx2[i]) % n
            ny = (tar_y + dy2[i]) % m
            if mat[nx][ny] != 0 and [nx, ny] != attacker:
                mat[nx][ny] = max(mat[nx][ny] - atk2, 0)
                attacked.append([nx, ny])

    return attacked


for r in range(1, k + 1):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mat[i][j] > 0:
                cnt += 1
    if cnt == 1:
        break

    attacker = pick_attacker()
    target = pick_target(attacker)
    recent[attacker[0]][attacker[1]] = r
    attacked = attack(attacker, target)

    ans = 0
    for i in range(n):
        for j in range(m):
            if [i, j] not in attacked and mat[i][j] != 0:
                mat[i][j] += 1
            if ans < mat[i][j]:
                ans = mat[i][j]

print(ans)
