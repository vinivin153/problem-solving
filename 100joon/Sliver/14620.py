import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
mat = [list(map(int, input().split())) for _ in range(n)]
res = 3000

points = []
for i in range(1, n - 1):
    for j in range(1, n - 1):
        points.append((i, j))


def calDist(a, b):
    x1, y1 = a
    x2, y2 = b
    if (abs(x1 - x2) + abs(y1 - y2)) < 3:
        return False
    else:
        return True


def sumCost(threePoints):
    sum1 = 0
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]
    for p in threePoints:
        x, y = p
        for i in range(5):
            nx = dx[i] + x
            ny = dy[i] + y
            sum1 += mat[nx][ny]
    return sum1


for p1, p2, p3 in combinations(points, 3):
    if calDist(p1, p2) and calDist(p2, p3) and calDist(p1, p3):
        sum1 = sumCost([p1, p2, p3])
        if res > sum1:
            res = sum1

print(res)
