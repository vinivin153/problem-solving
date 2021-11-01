# 921. Minimum Add to Make Parentheses Valid


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        cnt = 0
        for i in s:
            if i == "(":
                stack.append(1)
            else:
                if stack:
                    stack.pop()
                else:
                    cnt += 1

        return cnt + len(stack)
