n = int(input())

dp = [n] * (n + 1)
dp[1] = 0

for i in range(2, n + 1):
    a, b, c = dp[i - 1], n, n

    if i % 2 == 0:
        b = dp[i // 2]

    if i % 3 == 0:
        c = dp[i // 3]

    dp[i] = min(a, b, c) + 1

print(dp[n])
now = dp[n]
result = []
for i in range(n, 0, -1):
    if now == dp[i]:
        if not result:
            result.append(i)
            now -= 1
        elif result[-1] / 3 == i or result[-1] / 2 == i or result[-1] - 1 == i:
            result.append(i)
            now -= 1
print(*result)
