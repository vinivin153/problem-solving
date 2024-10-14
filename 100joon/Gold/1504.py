from heapq import heappush, heappop

n, e = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
a, b = map(int, input().split())

INF = 10**9


def dijkstra(start):
    dist = [INF] * (n + 1)

    heap = []
    # 우선순위와, 번호
    heappush(heap, (0, start))
    dist[start] = 0

    while heap:
        d, now = heappop(heap)

        if dist[now] < d:
            continue

        for next, cost in edges[now]:
            next_cost = d + cost
            if next_cost < dist[next]:
                dist[next] = next_cost
                heappush(heap, (next_cost, next))
    return dist


res1 = dijkstra(a)
res2 = dijkstra(b)
# start - a - b - n
cost1 = res1[1] + res1[b] + res2[n]
# start - b - a - n
cost2 = res2[1] + res2[a] + res1[n]


if cost1 >= INF and cost2 >= INF:
    print(-1)
else:
    print(min(cost1, cost2))
