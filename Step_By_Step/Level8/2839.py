n = int(input())
if n == 3:
    print(1)
elif n == 4:
    print(-1)
elif n == 5:
    print(1)
else:
    dp = [-1 for _ in range(n + 1)]
    dp[3] = dp[5] = 1
    for i in range(6, n + 1):
        if dp[i - 3] == -1 and dp[i - 5] == -1:
            dp[i] = -1
        elif dp[i - 3] != -1 and dp[i - 5] == -1:
            dp[i] = dp[i - 3] + 1
        elif dp[i - 3] == -1 and dp[i - 5] != -1:
            dp[i] = dp[i - 5] + 1
        else:
            dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    print(dp[n])
