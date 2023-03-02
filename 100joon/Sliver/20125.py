import sys

input = sys.stdin.readline

n = int(input())
mat = [list(input().rstrip()) for _ in range(n)]


def dfs(i, j):
    left_arm = 0
    right_arm = 0
    back = 0
    left_leg = 0
    right_leg = 0

    left = j - 1
    while 0 <= left and mat[i][left] == "*":
        left_arm += 1
        left -= 1

    right = j + 1
    while right < n and mat[i][right] == "*":
        right_arm += 1
        right += 1

    down = i + 1
    while down < n and mat[down][j] == "*":
        back += 1
        down += 1

    l_down = down
    while l_down < n and mat[l_down][j - 1] == "*":
        left_leg += 1
        l_down += 1

    r_down = down
    while r_down < n and mat[r_down][j + 1] == "*":
        right_leg += 1
        r_down += 1

    print(i + 1, j + 1)
    print(left_arm, right_arm, back, left_leg, right_leg)


def find_head():
    for i in range(n):
        for j in range(n):
            if mat[i][j] == "*":
                dfs(i + 1, j)
                return


find_head()
