import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
lec = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

ans = 0
heap = []
for _, start, end in lec:
    while heap:
        if heap[0] <= start:
            heappop(heap)
        else:
            break

    heappush(heap, end)
    ans = max(len(heap), ans)

print(ans)
