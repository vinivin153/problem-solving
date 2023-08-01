import sys
from heapq import heappush, heappop

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    time = [sys.maxsize] * (n + 1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((s, a))

    heapq = []
    heappush(heapq, (0, c))
    time[c] = 0
    cnt, res = 0, 0
    while heapq:
        x_time, x = heappop(heapq)
        if x_time < time[x]:
            continue

        for next_time, next_x in graph[x]:
            if x_time + next_time < time[next_x]:
                time[next_x] = x_time + next_time
                heappush(heapq, (time[next_x], next_x))

    for i in time:
        if i != sys.maxsize:
            cnt += 1
            if i > res:
                res = i
    print(cnt, res)
