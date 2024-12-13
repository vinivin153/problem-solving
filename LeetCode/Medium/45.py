class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        MAX = 10 ** 9
        dp = [MAX] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, min(i + 1, 1001)):
                if nums[i - j] >= j and dp[i - j] + 1 < dp[i]:
                    dp[i] = dp[i - j] + 1
        return dp[-1]
        