import sys

input = sys.stdin.readline
n = int(input())

mat = [list(input().rstrip()) for _ in range(n)]


def recur(x, y, n):
    k = mat[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if mat[i][j] != k:
                return (
                    "("
                    + recur(x, y, n // 2)
                    + recur(x, y + n // 2, n // 2)
                    + recur(x + n // 2, y, n // 2)
                    + recur(x + n // 2, y + n // 2, n // 2)
                    + ")"
                )

    return k


print(recur(0, 0, n))
