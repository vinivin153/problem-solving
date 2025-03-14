import sys
from heapq import heappop, heappush

input = sys.stdin.readline
V, E, P = map(int, input().split())
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    edges[b].append([a, c])



def dijkstra(start, end):
    dist = [sys.maxsize] * (V + 1)
    dist[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        current_dist, current = heappop(heap)
        
        if dist[current] < current_dist:
            continue
        
        for next, next_dist in edges[current]:
            sum_dist = current_dist + next_dist
            if dist[next] > sum_dist:
                dist[next] = sum_dist
                heappush(heap, [sum_dist, next])
    return dist[end]

shortest_dist = dijkstra(1, V)
start_to_p = dijkstra(1, P)
p_to_end = dijkstra(P, V)
if shortest_dist == start_to_p + p_to_end:
    print("SAVE HIM")
else:
    print("GOOD BYE")
