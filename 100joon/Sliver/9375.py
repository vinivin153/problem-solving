import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    clothes = defaultdict(list)
    for _ in range(n):
        name, cat = map(str, input().rstrip().split())
        clothes[cat].append(name)

    for i in clothes:
        res *= len(clothes[i]) + 1

    print(res - 1)
