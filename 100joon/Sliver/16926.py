import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n, m) // 2):
        x, y = i, i
        pre = mat[x][y]
        for j in range(i + 1, n - i):
            x = j
            temp = mat[x][y]
            mat[x][y] = pre
            pre = temp

        for j in range(i + 1, m - i):
            y = j
            temp = mat[x][y]
            mat[x][y] = pre
            pre = temp

        for j in range(i + 1, n - i):
            x = n - j - 1
            temp = mat[x][y]
            mat[x][y] = pre
            pre = temp

        for j in range(i + 1, m - i):
            y = m - j - 1
            temp = mat[x][y]
            mat[x][y] = pre
            pre = temp

for i in range(n):
    for j in range(m):
        print(mat[i][j], end=" ")
    print()
