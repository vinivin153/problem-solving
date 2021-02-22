n = int(input())
dp = [1 for _ in range(10)]

for i in range(n - 1):
    for j in range(8, -1, -1):
        dp[j] = dp[j] + dp[j + 1]

print(sum(dp) % 10007)
