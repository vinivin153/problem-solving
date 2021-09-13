class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt_L = 0
        cnt_R = 0
        cnt = 0
        for i in s:
            if i == "L":
                cnt_L += 1
            else:
                cnt_R += 1
            if cnt_L == cnt_R:
                cnt += 1

        return cnt
