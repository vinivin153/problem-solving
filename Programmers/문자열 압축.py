def calc_len(s, k):
    pre = ""
    count = 0
    result = 0

    for i in range(0, len(s) + k, k):
        w = s[i : i + k]

        if pre != w:
            if count == 1:
                result += len(pre)
            elif count > 1:
                result += len(pre) + len(str(count))
            pre = w
            count = 1
        else:
            count += 1

    return result


def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):
        answer = min(answer, calc_len(s, i))

    return answer
