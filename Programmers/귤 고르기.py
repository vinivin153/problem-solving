def solution(k, tangerine):
    s = {}
    for t in tangerine:
        if t not in s:
            s[t] = 1
        else:
            s[t] += 1

    s = sorted(s.items(), key=lambda x: -x[1])

    cnt = 0
    for i in range(len(s)):
        cnt += s[i][1]
        if cnt >= k:
            return i + 1
