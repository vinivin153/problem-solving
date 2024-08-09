n = [0] + list(input().rstrip()) + [""]
dp = [0] * len(n)
dp[0] = 1
dp[1] = 1
error = False

for i in range(2, len(n)):
    if n[i] == "0":
        if n[i - 1] not in ("1", "2"):
            error = True
            break
        dp[i] = dp[i - 1]
    elif n[i - 1] == "0":
        dp[i] = dp[i - 1]
    elif 10 <= int(n[i - 1] + n[i]) <= 26:
        if n[i + 1] != "0":
            dp[i] = dp[i - 2] + dp[i - 1]
        else:
            dp[i] = dp[i - 1]
    else:
        dp[i] = dp[i - 1]


if error or n[1] == "0":
    print(0)
else:
    print(dp[-1] % 1000000)
