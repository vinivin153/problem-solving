import sys
from collections import deque


def bfs(a):
    q = deque()
    q.append(a)
    visited = [0 for _ in range(n + 1)]
    visited[a] = 1
    cnt = 1
    while q:
        current = q.popleft()
        for i in com[current]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
                cnt += 1

    return cnt


n, m = map(int, sys.stdin.readline().split())

com = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    com[b].append(a)

result = []
max_cnt = 0
for i in range(1, n + 1):
    t = bfs(i)
    if max_cnt == t:
        result.append(i)
    if max_cnt < t:
        max_cnt = t
        result = []
        result.append(i)

# max_cnt = max(result)

# for i in range(1, n + 1):
#     if max_cnt == result[i]:
#         print(i, end=" ")

print(*result)
