# 451. Sort Characters By Frequency


class Solution:
    def frequencySort(self, s: str) -> str:
        alpha = {}
        result = []
        for i in s:
            if i in alpha:
                alpha[i] += 1
            else:
                alpha[i] = 1
        a = sorted(alpha.items(), key=lambda x: x[1], reverse=True)

        for i, v in a:
            for _ in range(v):
                result.append(i)

        result = "".join(result)

        return result
