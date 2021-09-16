# 1143. Longest Common Subsequence


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        memo_LCS = [[0 for _ in range(n)] for _ in range(m)]
        print(memo_LCS)

        def LCS(m, n):
            if m == -1 or n == -1:
                return 0
            elif text1[m] == text2[n]:
                if memo_LCS[m][n]:
                    return memo_LCS[m][n]
                else:
                    memo_LCS[m][n] = LCS(m - 1, n - 1) + 1
                    return memo_LCS[m][n]
            else:
                if memo_LCS[m][n]:
                    return memo_LCS[m][n]
                else:
                    memo_LCS[m][n] = max(LCS(m - 1, n), LCS(m, n - 1))
                    return memo_LCS[m][n]

        return LCS(m - 1, n - 1)
