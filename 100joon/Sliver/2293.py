n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * 10001
dp[0] = 1

for coin in coins:
    for i in range(1, k + 1):
        diff = i - coin
        if diff >= 0:
            dp[i] += dp[diff]

print(dp[k])
