from collections import defaultdict


class Solution(object):
    def removeDuplicates(self, nums):
        count = defaultdict(int)
        ans = []
        i = 0
        while i < len(nums):
            if count[nums[i]] >= 2:
                del nums[i]
                continue
            else:
                count[nums[i]] += 1
                ans.append(nums)

            i += 1

        return len(ans)
