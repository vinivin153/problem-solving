import sys

input = sys.stdin.readline
n = int(input())
m = [0] + [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (n + 1)
dp[1] = m[1][2]
for i in range(2, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + m[i][2])

print(dp[-1])
