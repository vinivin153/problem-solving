import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
p.insert(0, 0)

dp = [0 for _ in range(1001)]

dp[1] = p[1]
for i in range(2, n + 1):
    tmp = p[i]
    for j in range(1, i):
        if dp[i - j] + p[j] < tmp:
            tmp = dp[i - j] + p[j]
    dp[i] = tmp

print(dp[n])
