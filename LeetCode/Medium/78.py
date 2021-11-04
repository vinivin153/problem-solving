# 78. Subsets


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        visited = [0] * 10
        result = []

        def backtraking(v):
            r = []
            for i in range(len(nums)):
                if visited[i] == 1:
                    r.append(nums[i])
            result.append(r)
            for i in range(v, len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    backtraking(i)
                    visited[i] = 0

        backtraking(0)

        return result
