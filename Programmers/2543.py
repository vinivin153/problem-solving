import math


def solution(progresses, speeds):
    answer = []
    cnt = 0
    for i in range(len(progresses)):
        if progresses[i] >= 100:
            cnt += 1
            continue
        if cnt != 0:
            answer.append(cnt)
        cnt = 1
        left_day = math.ceil((100 - progresses[i]) / speeds[i])
        for j in range(i, len(progresses)):
            progresses[j] += speeds[j] * left_day
    answer.append(cnt)
    return answer
