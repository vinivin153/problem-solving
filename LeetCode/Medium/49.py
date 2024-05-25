from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ss = []
        for str in strs:
            ss.append("".join(sorted(str)))

        res = defaultdict(list)
        for i in range(len(ss)):
            res[ss[i]].append(strs[i])

        return res.values()
