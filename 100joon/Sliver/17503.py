import sys
import heapq

input = sys.stdin.readline

# m은 선호도 합 v는 선호도 c는 도수레벨
n, m, k = map(int, input().split())
beer = sorted([list(map(int, input().split())) for _ in range(k)], key=lambda x: x[1])
idx = -1

h = []
for i in range(n):
    idx += 1
    heapq.heappush(h, beer[idx][0])

hap = sum(h)
while True:
    if hap >= m:
        print(beer[idx][1])
        break
    else:
        if idx < len(beer) - 1:
            idx += 1
            heapq.heappush(h, beer[idx][0])
            x = heapq.heappop(h)
            if beer[idx][0] > x:
                hap = hap + beer[idx][0] - x
        else:
            print(-1)
            break
