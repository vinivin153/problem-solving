import sys

input = sys.stdin.readline

n = int(input())
cost = [0] + [list(map(int, input().split())) for _ in range(n)]
MAX = n + 1
dp = [0] * (n + 2)

max_value = [0] * (n + 2)
for i in range(n, 0, -1):
    t, p = cost[i]

    if t + i <= MAX:
        dp[i] = max_value[i + t] + p
    else:
        dp[i] = dp[i + 1]
    max_value[i] = max(dp[i], max_value[i + 1])


print(max(dp))
