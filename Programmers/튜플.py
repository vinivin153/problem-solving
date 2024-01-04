import re


def solution(s):
    # nums = s[2:-2].split('},{')
    nums = re.findall("\{([^{}]+)\}", s)
    ss = [set(map(int, num.split(","))) for num in nums]
    ss.sort(key=len)

    answer = [ss[0]]
    for i in range(len(ss) - 1):
        answer.append(ss[i + 1] - ss[i])

    return [next(iter(k)) for k in answer]
