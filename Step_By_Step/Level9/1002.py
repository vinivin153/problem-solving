import sys

t = int(input())
for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    d = (x2 - x1) ** 2 + (y2 - y1) ** 2
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    elif d > (r1 + r2) ** 2 or d < (r1 - r2) ** 2:
        print(0)
    elif d == (r1 + r2) ** 2 or d == (r1 - r2) ** 2:
        print(1)
    elif d < (r1 + r2) ** 2 or d > (r1 - r2) ** 2:
        print(2)