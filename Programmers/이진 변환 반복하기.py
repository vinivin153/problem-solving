answer = 0


def trans_bin(x):
    global answer
    a = x.count("0")
    answer += a
    b = len(x) - a

    return bin(b)[2:]


def solution(s):
    global answer
    cnt = 0

    while s != "1":
        s = trans_bin(s)
        cnt += 1

    return [cnt, answer]
