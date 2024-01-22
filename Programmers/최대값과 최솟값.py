def solution(s):
    ss = list(map(int, s.split()))
    return str(min(ss)) + " " + str(max(ss))
