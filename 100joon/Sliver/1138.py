import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
tall = [0] + list(map(int, input().split()))
info = {}

for i in range(1, n + 1):
    info[i] = tall[i]


for p in permutations(range(1, n + 1), n):
    for i in range(n):
        cnt = 0
        for j in range(i):
            if p[j] > p[i]:
                cnt += 1
        if cnt != info[p[i]]:
            break
    else:
        print(*p)
