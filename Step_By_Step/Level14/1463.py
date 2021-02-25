n = int(input())

dp = [n // 2 for _ in range(n + 1)]
dp[1] = 0

for i in range(1, n):
    if i * 3 <= n:
        dp[i * 3] = min(dp[i] + 1, dp[i * 3])
    if i * 2 <= n:
        dp[i * 2] = min(dp[i] + 1, dp[i * 2])
    if i + 1 <= n:
        dp[i + 1] = min(dp[i] + 1, dp[i + 1])

print(dp[n])
