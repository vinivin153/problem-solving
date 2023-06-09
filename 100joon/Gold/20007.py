"""
집들 사이에 양방향 도로 M개
X보다 멀지 않고 가장 가까운 집부터 방문
집에서 왕복할 수 있는 거리만
최소 며칠 소요되는가?
방문할 수 없는 경우 -1 출력
"""

import sys
from heapq import *

input = sys.stdin.readline
# n: 집의 수 m: 도로 수 x: 가능 거리 y: 성현 집
n, m, x, y = map(int, input().split())

roads = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    roads[a].append([b, c])
    roads[b].append([a, c])

# y에서 모든 집까지의 거리 구하기
dist = [10 ** 9] * n
dist[y] = 0
heap = []

heappush(heap, (dist[y], y))
while heap:
    cost, node = heappop(heap)

    if dist[node] < cost:
        continue

    for b, c in roads[node]:
        nc = c + cost
        if nc < dist[b]:
            dist[b] = nc
            heappush(heap, (nc, b))

dist.sort()

if dist[-1] * 2 > x:
    print(-1)
else:
    ans = 0
    cnt = 0
    for c in dist:
        nc = cnt + c * 2
        if x >= nc:
            cnt = nc
        else:
            cnt = c * 2
            ans += 1

    print(ans + 1)
