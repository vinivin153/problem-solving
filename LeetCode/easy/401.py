# 401. Binary Watch


class Solution:
    def readBinaryWatch(self, turnedOn: int):
        nums = [8, 4, 2, 1, 32, 16, 8, 4, 2, 1]
        visited = [0] * 10
        result = []

        def backtraking(v, n):
            if n == turnedOn:
                hap_h = 0
                hap_m = 0
                for i in range(4):
                    if visited[i] == 1:
                        hap_h += nums[i]
                for i in range(4, 10):
                    if visited[i] == 1:
                        hap_m += nums[i]
                if hap_h <= 11 and hap_m <= 59:
                    result.append(f"{hap_h}:{hap_m:02d}")

                return

            for i in range(v, 10):
                if visited[i] == 0:
                    visited[i] = 1
                    backtraking(i, n + 1)
                    visited[i] = 0

        backtraking(0, 0)

        return result
