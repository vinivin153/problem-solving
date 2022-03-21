import sys
from collections import deque

input = sys.stdin.readline


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        x = queue.popleft()
        for i in edge[x]:
            if visited[i] == 0:
                queue.append(i)
                if visited[x] == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    relation = []
    edge = [[] for _ in range(v + 1)]

    for _ in range(e):
        a, b = map(int, input().split())
        edge[a].append(b)
        edge[b].append(a)
        relation.append([a, b])

    visited = [0] * (v + 1)

    for i in range(1, v + 1):
        if visited[i] == 0:
            visited[i] = 1
            bfs(i)

    for i in relation:
        if visited[i[0]] == visited[i[1]]:
            print("NO")
            break
    else:
        print("YES")
