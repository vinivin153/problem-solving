# 338. Counting Bits


class Solution:
    def countBits(self, n: int) -> List[int]:
        if n == 0:
            return [0]

        dp = [0] * (n + 1)
        dp[1] = 1

        k = 2
        for i in range(2, n + 1):
            if i == (k * 2):
                k *= 2
            dp[i] = dp[i - k] + 1

        return dp
