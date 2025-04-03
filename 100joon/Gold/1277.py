import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n, w = map(int, input().split())
m = float(input())
factory = [0] + [list(map(int, input().split())) for _ in range(n)]
edges = [[] for _ in range(n + 1)]

for _ in range(w):
    a, b = map(int, input().split())
    edges[a].append([b, 0])
    edges[b].append([a, 0])

for i in range(1, n):
    for j in range(i + 1, n + 1):
        x1, y1 = factory[i]
        x2, y2 = factory[j]
        dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        if dist <= m:
            edges[i].append([j, dist])
            edges[j].append([i, dist])


dist = [sys.maxsize] * (n + 1)
dist[1] = 0


def dijkstra():
    heap = []
    heappush(heap, [dist[1], 1])
    while heap:
        now_cost, now = heappop(heap)

        if dist[now] < now_cost:
            continue

        for next, next_cost in edges[now]:
            cost = now_cost + next_cost
            if cost < dist[next]:
                dist[next] = cost
                heappush(heap, [cost, next])


dijkstra()
print(int(dist[n] * 1000))
