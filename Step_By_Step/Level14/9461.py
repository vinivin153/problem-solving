import sys

t = int(sys.stdin.readline())
dp = [1 for _ in range(101)]
for i in range(4, 101):
    dp[i] = dp[i - 2] + dp[i - 3]

for i in range(t):
    n = int(sys.stdin.readline())
    print(dp[n])