class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        if n <= 1:
            return s

        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start, end = 0, 1
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                isPalindrom = False
                if s[i] == s[j] and (i - j <= 2 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                    if max_len < (i - j + 1):
                        max_len = i - j + 1
                        start = j
                        end = i + 1

        return s[start:end]
