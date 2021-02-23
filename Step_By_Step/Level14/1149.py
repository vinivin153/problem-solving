import sys

n = int(sys.stdin.readline())
dp = list(map(int, sys.stdin.readline().split()))

for i in range(2, n + 1):
    r, g, b = map(int, sys.stdin.readline().split())
    x = min(dp[1], dp[2])
    y = min(dp[0], dp[2])
    z = min(dp[0], dp[1])
    dp[0] = r + x
    dp[1] = g + y
    dp[2] = b + z

print(min(dp))