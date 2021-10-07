# 997. Find the Town Judge


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [0] * (n + 1)
        b = [0] * (n + 1)
        for x, y in trust:
            a[x] += 1
            b[y] += 1

        for i in range(1, n + 1):
            if b[i] == n - 1 and a[i] == 0:
                return i

        return -1
