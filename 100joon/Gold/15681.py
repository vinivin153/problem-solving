import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, r, q = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)


def dfs(x):
    count = 1
    if not edges[x]:
        return count
    
    for i in edges[x]:
        if not visited[i]:
            visited[i] = 1
            count += dfs(i)
    
    visited[x] = count
    return count

visited = [0] * (n + 1)
visited[r] = 1
dfs(r)

for _ in range(q):
    u = int(input())
    print(visited[u])


