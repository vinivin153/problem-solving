import math
import sys

t = int(input())
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    x = math.ceil(n / h)
    y = n % h
    if y == 0:
        y = h
    print(f"{y}{x:02d}")
