import sys
from heapq import heappush, heappop

input = sys.stdin.readline
n = int(input())
circle = []
for _ in range(n):
    x, r = map(int, input().split())
    start, end = x - r, x + r
    circle.append([start, end])
circle.sort(key = lambda x : x[0])

heap = []
heappush(heap, -10 ** 7)

for start, end in circle:
    while heap:
        # 현재원이 외부에 있는 경우
        if heap[0] < start:
            heappop(heap)
        # 현재원이 이전 원 내부에 있는 경우
        else:
            break

    # 나의 end가 이전원의 end랑 같거나 큰 경우 = 겹침
    if heap and heap[0] <= end:
        print('NO')
        break
    
    heappush(heap, end)
else:
    print('YES')