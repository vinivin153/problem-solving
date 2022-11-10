# 개미와 진딧물
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]

ant = []
bug = []
for i in range(n):
    for j in range(n):
        if mat[i][j] == 1:
            ant.append([i, j])
        elif mat[i][j] == 2:
            bug.append([i, j])

cnt = 0
for x1, y1 in ant[:]:
    for x2, y2 in bug:
        if abs(x1 - x2) + abs(y1 - y2) <= m:
            cnt += 1
            break

print(cnt)
