import sys
from itertools import product

input = sys.stdin.readline

t = int(input())
nums = [i * (i + 1) // 2 for i in range(1, 46)]

for _ in range(t):
    n = int(input())
    k = 0
    for i in range(1, 46):
        if n < nums[i]:
            k = i
            break
    for p in product(nums[: k + 1], repeat=3):
        if sum(p) == n:
            print(1)
            break
    else:
        print(0)
