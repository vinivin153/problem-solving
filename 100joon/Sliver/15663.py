import sys
from itertools import permutations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = set()

for ss in permutations(arr, m):
    if ss in s:
        continue
    else:
        s.add(ss)
        print(*ss)
