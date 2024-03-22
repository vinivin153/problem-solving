from heapq import heappop, heappush


def solution(n, s, a, b, fares):
    MAX = 10**8

    nodes = [[] for _ in range(n + 1)]
    for aa, bb, cost in fares:
        nodes[aa].append((bb, cost))
        nodes[bb].append((aa, cost))

    def dijkstra(start):
        min_cost = [MAX] * (n + 1)
        min_cost[start] = 0
        heap = []
        heappush(heap, (min_cost[start], start))
        while heap:
            now_cost, now = heappop(heap)

            if now_cost > min_cost[now]:
                continue

            for next_node, next_cost in nodes[now]:
                cost = now_cost + next_cost
                if cost < min_cost[next_node]:
                    min_cost[next_node] = cost
                    heappush(heap, (cost, next_node))

        return min_cost

    S_cost = dijkstra(s)
    A_cost = dijkstra(a)
    B_cost = dijkstra(b)

    ans = MAX
    for node in range(1, n + 1):
        cost = S_cost[node] + B_cost[node] + A_cost[node]
        ans = min(cost, ans)

    return ans
