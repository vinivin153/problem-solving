# 771. Jewels and Stones
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        jewels = set(jewels)
        for i in stones:
            for j in jewels:
                if i in j:
                    cnt += 1
        return cnt
