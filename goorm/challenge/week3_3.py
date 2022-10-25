# 구름이의 여행
import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
bridge = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    bridge[a].append(b)
    bridge[b].append(a)

dist = [-1] * (n + 1)
dist[1] = 0

queue = deque()
queue.append(1)
while queue:
    x = queue.popleft()
    if x == n:
        break
    for i in bridge[x]:
        if dist[i] == -1:
            queue.append(i)
            dist[i] = dist[x] + 1

if dist[n] == -1 or dist[n] > k:
    print("NO")
else:
    print("YES")
