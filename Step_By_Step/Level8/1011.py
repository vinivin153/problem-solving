import math
import sys

t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    dx = b - a
    m = int(math.sqrt(dx))
    print(2 * (m - 1) + math.ceil((dx - (m * (m - 1))) / m))
