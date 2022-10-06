# 근묵자흑
import sys
import math

input = sys.stdin.readline
n, k = map(int, input().split())
nums = list(map(int, input().split()))

if k == 2:
    print(n - 1)
elif k == n:
    print(1)
else:
    print(math.ceil(((n - 1) / (k - 1))))
