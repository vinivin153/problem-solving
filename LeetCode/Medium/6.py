class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        ss = [[] for _ in range(numRows)]
        d = "down"
        level = 0
        for i in s:
            ss[level].append(i)
            if level == 0:
                d = "down"
                level += 1
            elif level == numRows - 1:
                d = "up"
                level -= 1
            else:
                if d == "down":
                    level += 1
                else:
                    level -= 1

        ans = ""
        for i in ss:
            ans += "".join(i)
        return ans