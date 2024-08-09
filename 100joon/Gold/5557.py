import sys

input = sys.stdin.readline
n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n)]
dp[1][nums[1]] = 1
for i in range(2, n):
    for j in range(21):
        if j + nums[i] <= 20:
            dp[i][j + nums[i]] += dp[i - 1][j]
        if j - nums[i] >= 0:
            dp[i][j - nums[i]] += dp[i - 1][j]
print(dp[-1][nums[-1]])
