h, y = map(int, input().split())


dp = [0] * (y + 1)
dp[0] = h
dp[1] = int(h * 1.05)

for i in range(2, y + 1):
    a = int(dp[i - 1] * 1.05)
    b = 0
    c = 0

    if i - 3 >= 0:
        b = int(dp[i - 3] * 1.2)
    if i - 5 >= 0:
        c = int(dp[i - 5] * 1.35)

    dp[i] = max(a, b, c)

print(dp[y])
