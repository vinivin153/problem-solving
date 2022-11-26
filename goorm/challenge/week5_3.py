# 수 이어 붙이기
import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
cards = list(map(str, input().split()))

min_num = sys.maxsize
for p in permutations(cards, n):
    s = p[0]
    for i in range(1, n):
        if p[i - 1][1] == p[i][0]:
            s += p[i][1]
        else:
            s += p[i]
    if int(min_num) > int(s):
        min_num = int(s)
print(min_num)
