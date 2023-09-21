import sys

input = sys.stdin.readline
# 격자, 진행되는 횟수, 제초제 범위, 제초제 남아있는 년 수
n, m, k, c = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def grow_tree():
    for x in range(n):
        for y in range(n):
            # 나무인 경우
            if mat[x][y] > 0:
                cnt = 0
                # 주변 나무 수 세는 작업
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if mat[nx][ny] > 0:
                            cnt += 1
                mat[x][y] += cnt


def spread_tree():
    # 번식할 나무
    wait_trees = []
    for x in range(n):
        for y in range(n):
            # 나무인 경우
            if mat[x][y] > 0:
                cnt = 0
                temp = []
                # 번식 가능한 칸 찾기
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        # 번식 가능한 칸(빈칸)
                        if mat[nx][ny] == 0:
                            cnt += 1
                            temp.append([nx, ny])
                # 번식하는 나무의 값
                if cnt:
                    value = mat[x][y] // cnt
                    for a, b in temp:
                        wait_trees.append([a, b, value])
    for tree in wait_trees:
        a, b, value = tree
        mat[a][b] += value


dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, -1, 1]


def find_killer_pos():
    count_kill_trees = []
    for x in range(n):
        for y in range(n):
            # 나무인 경우
            if mat[x][y] > 0:
                # 박멸될 나무의 수
                cnt = mat[x][y]
                for i in range(4):
                    # 대각선 범위
                    for j in range(1, k + 1):
                        nx = x + dx2[i] * j
                        ny = y + dy2[i] * j

                        if not (0 <= nx < n and 0 <= ny < n):
                            break

                        # 빈칸이거나 벽인 경우
                        if mat[nx][ny] == 0 or mat[nx][ny] == -1:
                            break

                        # 제초제 뿌린 경우
                        if mat[nx][ny] <= -10:
                            break

                        cnt += mat[nx][ny]
                count_kill_trees.append([cnt, x, y])
    count_kill_trees.sort(key=lambda x: (-x[0], x[1], x[2]))
    return [count_kill_trees[0][1], count_kill_trees[0][2]]


def kill_trees(killer):
    global ans
    x, y = killer
    kill = c * -10
    ans += mat[x][y]
    mat[x][y] = kill

    for i in range(4):
        for j in range(1, k + 1):
            nx = x + dx2[i] * j
            ny = y + dy2[i] * j

            if not (0 <= nx < n and 0 <= ny < n):
                break

            if mat[nx][ny] == -1:
                break

            if mat[nx][ny] <= 0:
                mat[nx][ny] = kill
                break

            ans += mat[nx][ny]
            mat[nx][ny] = kill


def decrease_kill_time():
    for i in range(n):
        for j in range(n):
            if mat[i][j] <= -10:
                mat[i][j] += 10


def check_trees():
    for i in range(n):
        for j in range(n):
            if mat[i][j] > 0:
                return False
    return True


for i in range(m):
    if check_trees():
        break
    grow_tree()
    spread_tree()
    decrease_kill_time()
    killer = find_killer_pos()
    kill_trees(killer)


print(ans)
