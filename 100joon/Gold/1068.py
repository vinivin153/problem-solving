import sys
from collections import defaultdict

n = int(input())
parents = list(map(int, input().split()))
relation = [[] for _ in range(n)]
for child, parent in enumerate(parents):
    if parent != -1:
        relation[parent].append(child)
rid = int(input())

if parents[rid] == -1:
    print(0)
    sys.exit()

leaf = defaultdict(int)


def dfs(k):
    if not relation[k]:
        leaf[k] = 1
        return 1

    for i in relation[k]:
        leaf[k] += dfs(i)

    return leaf[k]


total = dfs(parents.index(-1))
if leaf[rid] == leaf[parents[rid]]:
    total += 1

print(total - leaf[rid])
