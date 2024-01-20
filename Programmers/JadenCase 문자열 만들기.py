import re


def solution(s):
    ss = list(map(str, s.lower().split()))
    blank = re.findall('[" "]+', s) + [""]

    for i in range(len(ss)):
        ss[i] = ss[i][0].upper() + ss[i][1:] + blank[i]

    return "".join(ss)
