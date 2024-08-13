import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
names = sorted(list(map(str, input().split())))
family = {name: [] for name in names}
child = {name: [] for name in names}
count_parent = {name: 0 for name in names}

m = int(input())
for _ in range(m):
    a, b = map(str, input().split())
    count_parent[a] += 1
    family[b].append(a)

top = []
queue = deque()
for name in names:
    # 가장 위의 조상을 찾기
    if count_parent[name] == 0:
        queue.append(name)
        top.append(name)

while queue:
    name = queue.popleft()
    for next in family[name]:
        count_parent[next] -= 1
        if count_parent[next] == 0:
            child[name].append(next)
            queue.append(next)

print(len(top))
print(*sorted(top))
for name in names:
    print(f"{name} {len(child[name])}", end=" ")
    print(*sorted(child[name]))
