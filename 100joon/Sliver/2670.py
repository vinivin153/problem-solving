import sys

input = sys.stdin.readline
n = int(input())
nums = [round(float(input()), 2) for _ in range(n)]
dp = [1] * n
dp[0] = nums[0]

for i in range(1, n):
    if dp[i - 1] <= 1:
        dp[i] = nums[i]
    else:
        dp[i] = dp[i - 1] * nums[i]

print(f"{max(dp):.3f}")
