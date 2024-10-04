class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0

        left, right = 0, len(height) - 1
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            value = width * h
            ans = max(ans, value)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return ans
