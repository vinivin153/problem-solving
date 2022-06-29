# 해시 - 위장

from itertools import combinations


def solution(clothes):
    dress = {}
    for v, k in clothes:
        if k in dress:
            dress[k] += 1
        else:
            dress[k] = 1

    answer = 1

    for key in dress.keys():
        answer *= dress[key] + 1

    return answer - 1
