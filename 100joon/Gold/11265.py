"""
다익스트라 풀이방법 6524ms

import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n, m = map(int, input().split())
MAX = 10**9
mat = [list(map(int, input().split())) for _ in range(n)]
for _ in range(m):
    # 손님 위치, 이동할 곳, 남은시간
    a, b, c = map(int, input().split())

    dist = [MAX] * (n + 1)
    dist[a] = 0

    heap = []
    heappush(heap, [0, a])
    while heap:
        now_dist, now_loc = heappop(heap)

        if now_dist > dist[now_loc]:
            continue

        for next_loc, next_dist in enumerate(mat[now_loc - 1], 1):
            new_dist = now_dist + next_dist
            if new_dist < dist[next_loc] and new_dist <= c:
                dist[next_loc] = new_dist
                heappush(heap, [new_dist, next_loc])

    if dist[b] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
"""

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
MAX = 10**9
mat = [list(map(int, input().split())) for _ in range(n)]

for k in range(n):
    for a in range(n):
        for b in range(n):
            mat[a][b] = min(mat[a][b], mat[a][k] + mat[k][b])

for _ in range(m):
    # 손님 위치, 이동할 곳, 남은시간
    a, b, c = map(int, input().split())

    if mat[a - 1][b - 1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")
