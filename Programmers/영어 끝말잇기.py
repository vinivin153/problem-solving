import math


def solution(n, words):
    log = set()
    log.add(words[0])

    for i in range(1, len(words)):
        if words[i - 1][-1] != words[i][0] or words[i] in log:
            return [i % n + 1, math.ceil((i + 1) / n)]
        else:
            log.add(words[i])

    return [0, 0]
