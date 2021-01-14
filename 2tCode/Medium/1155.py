class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        arr = [[0 for i in range(target + 1)] for j in range(d)]

        for i in range(1, f + 1) if target >= f else range(1, target + 1):
            arr[0][i] = 1

        for i in range(1, d):
            for j in range(target + 1):
                if j - f <= 0:
                    arr[i][j] = sum(arr[i - 1][:j])
                elif j - f > 0:
                    arr[i][j] = sum(arr[i - 1][j - f : j])

        return arr[d - 1][target] % (10 ** 9 + 7)
