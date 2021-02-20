import sys

n = int(input())

dp = list(map(int, sys.stdin.readline().split()))
dp.insert(0, 0)

for i in range(1, n + 1):
    for j in range(1, (i // 2) + 1):
        if dp[i] < dp[j] + dp[i - j]:
            dp[i] = dp[j] + dp[i - j]
        # dp[i] = max(dp[j] + dp[i - j], dp[i])
print(dp[n])
