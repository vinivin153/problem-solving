def flip(s):
    result = ""
    for i in s:
        if i == "(":
            result += ")"
        else:
            result += "("

    return result


def solution(p):
    def trans(s):
        if s == "":
            return s

        # 나누는 u, v로 나누는 작업
        left = 0
        right = 0
        u, v = "", ""
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                u = s[: i + 1]
                v = s[i + 1 :]
                break

        stack = []
        isPerfect = True
        for i in u:
            if i == "(":
                stack.append(i)
            elif stack:
                stack.pop()
            else:
                isPerfect = False
                break

        # u가 올바른 문자열인 경우
        if isPerfect:
            return u + trans(v)
        else:
            # 올바른 문자열이 아닌 경우
            return "(" + trans(v) + ")" + flip(u[1:-1])

    return trans(p)
