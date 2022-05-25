from collections import deque

alpha = ["A", "E", "I", "O", "U"]
ans = []


def backTracking(kk, cnt):
    if cnt > 5:
        return
    else:
        ans.append(kk)

    for i in range(5):
        backTracking(kk + alpha[i], cnt + 1)


def solution(word):
    backTracking("", 0)
    return ans.index(word)
