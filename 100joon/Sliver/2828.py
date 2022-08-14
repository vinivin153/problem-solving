import sys

input = sys.stdin.readline
n, m = map(int, input().split())
k = int(input())

res = 0
cur = 1
for i in range(k):
    loc = int(input())
    if cur + m - 1 < loc:
        res += loc - (cur + m - 1)
        cur = loc - m + 1
    elif loc < cur:
        res += cur - loc
        cur = loc

print(res)
