# 1464. Maximum Product of Two Elements in an Array


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = nums.index(max(nums))
        k = 0
        for i in range(len(nums)):
            if k < nums[i] and i != m:
                k = nums[i]
        return (nums[m] - 1) * (k - 1)


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)
