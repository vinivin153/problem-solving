# 최소비용 구하기
import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
m = int(input())
bus = [[] for _ in range(n + 1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    bus[start].append([end, cost])


a, b = map(int, input().split())
dist = [sys.maxsize] * (n + 1)
dist[a] = 0
heap = []
heappush(heap, (0, a))

while heap:
    c, x = heappop(heap)

    if dist[x] < c:
        continue

    for nx, nc in bus[x]:
        nd = c + nc
        if nd < dist[nx]:
            dist[nx] = nd
            heappush(heap, (nd, nx))

print(dist[b])
