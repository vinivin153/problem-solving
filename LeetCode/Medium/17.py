class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        alpha = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        ans = []

        def backtracking(cnt, s):
            if cnt == len(digits):
                ans.append(s)
                return

            for i in alpha[digits[cnt]]:
                backtracking(cnt + 1, s + i)

        backtracking(0, "")

        return ans
