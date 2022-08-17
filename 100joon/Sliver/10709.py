import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

check_c = [-1] * n
for i in range(m):
    for j in range(n):
        if mat[j][i] == "c":
            check_c[j] = 1
            mat[j][i] = 0
        else:
            if check_c[j] != -1:
                mat[j][i] = check_c[j]
                check_c[j] += 1
            else:
                mat[j][i] = -1

for i in range(n):
    print(*mat[i])
