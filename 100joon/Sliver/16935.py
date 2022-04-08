import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

mat = []

for _ in range(n):
    mat.append(list(map(int, input().split())))


def up_down():
    for i in range(n // 2):
        mat[i], mat[n - i - 1] = mat[n - i - 1], mat[i]
    return mat


def left_right():
    for i in range(n):
        mat[i].reverse()
    return mat


def rotate_right():
    global m, n
    ret = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ret[j][n - i - 1] = mat[i][j]
    n, m = m, n
    return ret


def rotate_left():
    global m, n
    ret = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            ret[m - j - 1][i] = mat[i][j]
    n, m = m, n
    return ret


def move_right():
    ret = [[0] * m for _ in range(n)]
    nn = n // 2
    mm = m // 2
    for i in range(nn):
        ret[i][:mm] = mat[nn + i][:mm]
        ret[i][mm:] = mat[i][:mm]
        ret[nn + i][mm:] = mat[i][mm:]
        ret[nn + i][:mm] = mat[nn + i][mm:]
    return ret


def move_left():
    ret = [[0] * m for _ in range(n)]
    nn = n // 2
    mm = m // 2
    for i in range(nn):
        ret[i][:mm] = mat[i][mm:]
        ret[i][mm:] = mat[nn + i][mm:]
        ret[nn + i][mm:] = mat[nn + i][:mm]
        ret[nn + i][:mm] = mat[i][:mm]
    return ret


nums = list(map(int, input().split()))

for i in nums:
    if i == 1:
        mat = up_down()
    elif i == 2:
        mat = left_right()
    elif i == 3:
        mat = rotate_right()
    elif i == 4:
        mat = rotate_left()
    elif i == 5:
        mat = move_right()
    else:
        mat = move_left()

for i in range(n):
    print(*mat[i])
