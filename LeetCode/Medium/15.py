from itertools import combinations
from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ss = Counter(nums)
        ans = set()
        if ss[0] >= 3:
            ans.add((0, 0, 0))
        for i in combinations(set(nums), 2):
            a, b = i
            v = a + b
            vv = v * -1

            if a == 0 and b == 0:
                if ss[0] >= 3:
                    ans.add((0, 0, 0))
                continue

            if vv == a or vv == b:
                if ss[vv] >= 2:
                    ans.add(tuple(sorted([a, b, vv])))
                continue

            if vv in ss:
                ans.add(tuple(sorted([a, b, vv])))

        return ans
