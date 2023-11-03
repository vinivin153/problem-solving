from heapq import heappush, heappop


def solution(N, road, K):
    mat = [[] for _ in range(N + 1)]
    for r in road:
        a, b, c = r
        mat[a].append([b, c])
        mat[b].append([a, c])

    dist = [500001] * (N + 1)
    dist[1] = 0
    heap = []
    for i in mat[1]:
        b, c = i
        heappush(heap, (c, 1, b))

    while heap:
        c, a, b = heappop(heap)
        if dist[b] > dist[a] + c:
            dist[b] = dist[a] + c
            for i in mat[b]:
                x, y = i
                heappush(heap, (y, b, x))

    ans = 0
    for i in dist[1:]:
        if i <= K:
            ans += 1

    return ans
