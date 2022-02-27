import sys

n = int(input())

dp = [0 for _ in range(n + 1)]

dp[1] = 1
for i in range(2, n + 1):
    min_val = sys.maxsize
    for j in range(1, int(i ** 0.5) + 1):
        if min_val > dp[i - j ** 2]:
            min_val = dp[i - j ** 2]
    dp[i] = min_val + 1

print(dp[n])
