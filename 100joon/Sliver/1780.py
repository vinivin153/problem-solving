import sys

input = sys.stdin.readline
n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]

paper = {-1: 0, 0: 0, 1: 0}


def is_all_same(x, y, size):
    num = mat[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if mat[i][j] != num:
                return False
    return True


def find_square(x, y, size):
    global minus, zero, plus
    if size == 1:
        paper[mat[x][y]] += 1
        return

    if is_all_same(x, y, size):
        paper[mat[x][y]] += 1
        return
    else:
        sep_size = size // 3
        for i in range(x, x + size, sep_size):
            for j in range(y, y + size, sep_size):
                find_square(i, j, sep_size)


find_square(0, 0, n)
for cnt_paper in paper.values():
    print(cnt_paper)
