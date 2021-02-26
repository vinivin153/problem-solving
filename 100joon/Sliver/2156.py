import sys

n = int(sys.stdin.readline())
wine = [0]
dp = [0 for _ in range(n + 1)]
for _ in range(n):
    wine.append(int(sys.stdin.readline()))

dp[1] = wine[1]
if n != 1:
    dp[2] = dp[1] + wine[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + wine[i - 1] + wine[i], dp[i - 2] + wine[i], dp[i - 1])

print(max(dp[-1], dp[-2]))
