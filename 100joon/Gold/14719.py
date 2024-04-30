import sys

input = sys.stdin.readline
n, m = map(int, input().split())
height = list(map(int, input().split()))


mat = [[False] * m for _ in range(n)]
for i in range(m):
    for j in range(height[i]):
        mat[n - 1 - j][i] = True

cnt = 0
for i in range(n):
    prev = -1
    for j in range(m):
        if mat[i][j]:
            if prev == -1:
                prev = j
            else:
                cnt += j - prev - 1
                prev = j

print(cnt)
