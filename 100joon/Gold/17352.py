import sys
from collections import deque

n = int(input())


bridge = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

start = 0
for i in range(n - 2):
    a, b = map(int, sys.stdin.readline().split())
    bridge[a].append(b)
    bridge[b].append(a)
    start = b

queue = deque()
queue.append(start)
visited[start] = 1
while queue:
    x = queue.popleft()
    for i in bridge[x]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1


for i in range(1, n + 1):
    if visited[i] == 0:
        if start != 0:
            print(i, start)
            break
        else:
            print(1, 2)
            break
