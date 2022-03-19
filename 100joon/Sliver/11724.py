import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    queue = deque()
    queue.append(x)
    visited[x] = 1
    while queue:
        x = queue.popleft()
        for i in vertex[x]:
            if visited[i] == 0:
                visited[i] = 1
                queue.append(i)


n, m = map(int, input().split())
vertex = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)

cnt = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)
