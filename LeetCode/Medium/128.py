from heapq import heapify, heappop

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapify(nums)
        ans = 0
        max_len = 0
        prev = 10 ** 10 * -1
        while nums:
            x = heappop(nums)
            if prev + 1 == x:
                max_len += 1
            elif prev == x:
                pass
            else:
                ans = max(max_len, ans)
                max_len = 1

            prev = x
        
        ans = max(max_len, ans)
        return ans