import sys
from heapq import *

input = sys.stdin.readline

n, m, X = map(int, input().split())
bridge_go = [[] for _ in range(n + 1)]
bridge_back = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    bridge_go[a].append([c, b])
    bridge_back[b].append([c, a])


def dijkstra(bridge, k):
    dist = [sys.maxsize] * (n + 1)
    dist[k] = 0
    heap = []
    heappush(heap, (0, k))
    while heap:
        c, x = heappop(heap)

        if dist[x] < c:
            continue

        for nc, nx in bridge[x]:
            nd = c + nc

            if dist[nx] > nd:
                dist[nx] = nd
                heappush(heap, (nd, nx))
    return dist


res_go = dijkstra(bridge_go, X)
res_back = dijkstra(bridge_back, X)


res = 0

for i in range(1, n + 1):
    d = res_go[i] + res_back[i]
    if res < d:
        res = d

print(res)
