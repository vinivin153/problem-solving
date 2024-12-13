class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = False
        visited = [False] * n
        def find(x):
            nonlocal ans
            if x == 0:
                ans = True
                return
            
            for i in range(x - 1, -1, -1):
                if i + nums[i] >= x and not visited[i]:
                    visited[i] = True
                    find(i)
                    if ans:
                        return

        find(n - 1)
        return ans