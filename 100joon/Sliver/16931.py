import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
for i in range(1, n + 1):
    mat[i][1 : m + 1] = list(map(int, input().split()))

ans = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        pre = mat[i][j - 1]
        curent = mat[i][j]
        nxt = mat[i][j + 1]
        if curent > pre:
            ans += curent - pre
        if curent > nxt:
            ans += curent - nxt

for j in range(1, m + 1):
    for i in range(1, n + 1):
        pre = mat[i - 1][j]
        curent = mat[i][j]
        nxt = mat[i + 1][j]
        if curent > pre:
            ans += curent - pre
        if curent > nxt:
            ans += curent - nxt

ans += n * m * 2
print(ans)
