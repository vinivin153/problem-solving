# 121. Best Time to Buy and Sell Stock


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        min_value = prices[0]

        for i in range(1, len(prices)):
            if prices[i] - min_value > max_diff:
                max_diff = prices[i] - min_value
            if prices[i] < min_value:
                min_value = prices[i]

        return max_diff
