import sys

n = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
dp[1] = int(sys.stdin.readline())
for i in range(2, n + 1):
    value = [0] + list(map(int, sys.stdin.readline().split()))
    dp[i] = dp[i - 1] + value[-1]
    for j in range(i - 1, 1, -1):
        dp[j] = max(dp[j - 1], dp[j]) + value[j]
    dp[1] += value[1]

print(max(dp))
