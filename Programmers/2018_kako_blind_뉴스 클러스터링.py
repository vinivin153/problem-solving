from collections import defaultdict


def solution(str1, str2):
    str1 = "".join([i.lower() for i in str1])
    str2 = "".join([i.lower() for i in str2])

    s1, s2 = defaultdict(int), defaultdict(int)
    for i in range(len(str1) - 1):
        if str1[i : i + 2].isalpha():
            s1[str1[i : i + 2]] += 1

    for i in range(len(str2) - 1):
        if str2[i : i + 2].isalpha():
            s2[str2[i : i + 2]] += 1

    intersection, union = 0, 0
    for k, v in s1.items():
        if k in s2:
            intersection += min(v, s2[k])
            union += max(v, s2[k])
        else:
            union += v

    for k, v in s2.items():
        if k not in s1:
            union += v

    if not union:
        return 65536

    return int(intersection / union * 65536)
