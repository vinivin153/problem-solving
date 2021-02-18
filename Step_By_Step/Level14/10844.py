n = int(input())

dp = []
dp.append([1 for _ in range(12)])
dp[0][0] = dp[0][1] = dp[0][-1] = 0
for i in range(100):
    dp.append([0 for _ in range(12)])
for i in range(1, n):
    for j in range(1, 11):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
print(sum(dp[n - 1]) % 1000000000)
