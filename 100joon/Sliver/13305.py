import sys

input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [0] * (n - 1)
dp[0] = cost[0] * dist[0]
pre = cost[0]
for i in range(1, n - 1):
    if pre < cost[i]:
        dp[i] = dp[i - 1] + pre * dist[i]
    else:
        dp[i] = dp[i - 1] + cost[i] * dist[i]
        pre = cost[i]

print(dp[-1])
