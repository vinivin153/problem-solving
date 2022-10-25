# 순환하는 수로
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
waterways = [[] for _ in range(n + 1)]
for _ in range(n):
    a, b = map(int, input().split())
    waterways[a].append(b)
    waterways[b].append(a)
visited = set()
visited.add(1)
dist = [0] * (n + 1)
dist[1] = 1
ans = []

flag = 0


def dfs(current):
    global flag
    for i in waterways[current]:
        if flag:
            return
        if dist[i] == 0:
            dist[i] = dist[current] + 1
            visited.add(i)
            dfs(i)
            visited.remove(i)
            dist[i] = 0
        elif dist[current] - dist[i] >= 2:
            for j in visited:
                if dist[i] <= dist[j] <= dist[current]:
                    ans.append(j)
            flag = 1


dfs(1)
print(len(ans))
print(*sorted(ans))
