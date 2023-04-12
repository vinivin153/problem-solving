import sys
from collections import deque

input = sys.stdin.readline

n, d, k, c = map(int, input().split())

plate = []
for _ in range(n):
    plate.append(int(input()))

sushi = deque(plate[:k])
ans = len(set(sushi))
for i in range(k, n + k):
    sushi.popleft()
    sushi.append(plate[i % n])
    sushi_set = set(sushi)
    sushi_set.add(c)
    t = len(sushi_set)
    if ans < t:
        ans = t

print(ans)
