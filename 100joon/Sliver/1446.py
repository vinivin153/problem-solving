import sys

input = sys.stdin.readline


n, d = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
roads.sort(key=lambda x: (x[1], x[0]))

dp = [i for i in range(d + 1)]
for i in range(1, d + 1):
    dp[i] = dp[i - 1] + 1
    for start, end, dist in roads:
        if end > i:
            break

        if end == i:
            dp[i] = min(dp[i], dp[start] + dist)

print(dp[d])
