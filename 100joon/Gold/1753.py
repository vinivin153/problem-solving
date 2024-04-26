import sys
from heapq import heappop, heappush

input = sys.stdin.readline
INF = 10**8

v, e = map(int, input().split())
start = int(input())
mat = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b, w = map(int, input().split())
    mat[a].append((b, w))

dist = [INF] * (v + 1)
dist[start] = 0


def dijkstra():
    heap = []
    heappush(heap, (0, start))
    while heap:
        now_dist, now = heappop(heap)
        if now_dist > dist[now]:
            continue

        for next, next_dist in mat[now]:
            d = now_dist + next_dist
            if d < dist[next]:
                dist[next] = d
                heappush(heap, (d, next))


dijkstra()
for i in range(1, v + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
