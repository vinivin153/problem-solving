from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapify(nums)

        ans = 0
        for i in range(len(nums) - k + 1):
            ans = heappop(nums)

        return ans
