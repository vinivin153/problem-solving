# 39. Combination Sum


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(v, l):
            if v == 0:
                result.append(s[:])
                return

            for i in range(l, len(candidates)):
                if v - candidates[i] >= 0:
                    s.append(candidates[i])
                    backtracking(v - candidates[i], i)
                    s.pop()
                else:
                    return

        candidates.sort()
        result = []
        s = []

        backtracking(target, 0)

        return result
