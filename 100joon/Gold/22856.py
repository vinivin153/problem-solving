import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
parent = {}
parent[1] = 1
edges = defaultdict(list)
left_node = set()
for _ in range(n):
    a, b, c = map(int, input().split())
    left_node.add(a)
    edges[a].append(b)
    edges[a].append(c)
    if b != -1:
        parent[b] = a

    if c != -1:
        parent[c] = a

child_visited = set()
child_visited.add(-1)  # -1인 경우 방문처리

cnt = 0


def dfs(x):
    global cnt
    stack = []
    stack.append(x)
    while stack:
        x = stack.pop()

        child_left, child_right = edges[x]
        if child_left not in child_visited:
            stack.append(child_left)
            cnt += 1
            continue

        if x in left_node:
            left_node.remove(x)
        if not left_node:
            return
        child_visited.add(x)

        if child_right not in child_visited:
            stack.append(child_right)
            cnt += 1
            continue

        stack.append(parent[x])
        cnt += 1


dfs(1)
print(cnt)
