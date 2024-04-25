import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort()

dp = [100000] * (k + 1)
for coin in coins:
    if coin > k:
        break
    dp[coin] = 1

for i in range(1, k + 1):
    for coin in coins:
        if coin == i:
            continue
        else:
            if i - coin > 0 and dp[i - coin]:
                dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[k] == 100000:
    print(-1)
else:
    print(dp[k])
