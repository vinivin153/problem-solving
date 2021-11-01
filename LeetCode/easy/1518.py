# 1518. Water Bottles


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        emptyBottles = 0
        cnt = 0

        while numBottles != 0 and emptyBottles < numExchange:
            # drink
            cnt += numBottles
            emptyBottles += numBottles
            numBottles = 0

            # exchange
            numBottles = emptyBottles // numExchange
            emptyBottles = emptyBottles % numExchange

        return cnt
