"""
1번 상하 반전
2번 좌우 반전
3번 오른쪽 90도 회전
4번 왼쪽 90도 회전
5번 4분의 1로 나눠 그룹끼리 오른쪽 90도 회전
6번 4분의 1로 나눠 그룹끼리 왼쪽으로 90도 회전
"""


import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]


def up_down():
    global mat
    mat = mat[::-1]


def left_right():
    global mat
    mat = list(i[::-1] for i in mat)


def rotate_right():
    global n, m, mat
    mat = list(map(list, zip(*mat[::-1])))
    n, m = m, n


def rotate_left():
    global n, m, mat
    mat = list(map(list, zip(*mat)))[::-1]
    n, m = m, n


def group_rotate_right():
    global mat
    half_n = n // 2
    half_m = m // 2
    temp1 = list(i[:half_m] for i in mat[:half_n])
    temp2 = list(i[half_m:] for i in mat[:half_n])
    temp3 = list(i[half_m:] for i in mat[half_n:])
    temp4 = list(i[:half_m] for i in mat[half_n:])

    new_mat1 = [temp4[i] + temp1[i] for i in range(half_n)]
    new_mat2 = [temp3[i] + temp2[i] for i in range(half_n)]
    mat = new_mat1 + new_mat2


def group_rotate_left():
    global mat
    half_n = n // 2
    half_m = m // 2
    temp1 = list(i[:half_m] for i in mat[:half_n])
    temp2 = list(i[half_m:] for i in mat[:half_n])
    temp3 = list(i[half_m:] for i in mat[half_n:])
    temp4 = list(i[:half_m] for i in mat[half_n:])

    new_mat1 = [temp2[i] + temp3[i] for i in range(half_n)]
    new_mat2 = [temp1[i] + temp4[i] for i in range(half_n)]
    mat = new_mat1 + new_mat2


order = list(map(int, input().split()))
for i in order:
    if i == 1:
        up_down()
    elif i == 2:
        left_right()
    elif i == 3:
        rotate_right()
    elif i == 4:
        rotate_left()
    elif i == 5:
        group_rotate_right()
    else:
        group_rotate_left()

for i in mat:
    print(*i)
