import sys

input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
visited = [set() for _ in range(k + 1)]
bags = []
for i in range(n):
    w, v = map(int, input().split())
    bags.append((i, w, v))
bags.sort(key=lambda x: (x[1], x[2]))


for i in range(1, k + 1):
    for bag in bags:
        idx, w, v = bag
        if i - w < 0:
            break

        q = dp[i - w] + v
        if idx not in visited[i - w] and q > dp[i]:
            dp[i] = q
            visited[i] = visited[i - w] | set([idx])

print(max(dp))
