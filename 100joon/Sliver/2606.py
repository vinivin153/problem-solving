import sys

com = int(input())
n = int(input())
edge = {}
for i in range(1, com + 1):
    edge[i] = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)

stack = []
visited = {}
cnt = 0

stack.append(1)
while stack:
    current = stack.pop()
    visited[current] = 1
    cnt += 1
    neighbor = edge[current]
    if not neighbor:
        break
    for i in neighbor:
        if not i in visited and not i in stack:
            stack.append(i)

print(cnt - 1)
