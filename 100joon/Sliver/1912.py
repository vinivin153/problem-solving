n = int(input())
nums = list(map(int, input().split()))

dp = [-1001] * (n + 1)
dp[1] = nums[0]

for i in range(2, n + 1):
    dp[i] = max(nums[i - 1], nums[i - 1] + dp[i - 1])

print(max(dp))
