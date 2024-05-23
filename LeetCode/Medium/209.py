class Solution(object):
    def minSubArrayLen(self, target, nums):
        MAX = 10**5 + 1
        ans = MAX
        n = len(nums)
        start, end = 0, 0
        value = nums[start]

        while end < n:
            if value >= target:
                ans = min(end - start + 1, ans)
                if ans == 1:
                    print(value, start, end)
                    break
                value -= nums[start]
                start += 1
            else:
                if end == n - 1:
                    break
                end += 1
                value += nums[end]

        if ans == MAX:
            return 0
        else:
            return ans
