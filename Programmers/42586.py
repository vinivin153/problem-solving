# 스택/큐 기능개발

from collections import deque
import math


def solution(progresses, speeds):
    queue = deque(progresses)
    s = deque(speeds)
    l = len(progresses)
    answer = []
    cnt = 0
    while queue:
        k = math.ceil((100 - queue[0]) / s[0])
        for i in range(l):
            queue[i] += s[i] * k

        while queue and queue[0] >= 100:
            queue.popleft()
            s.popleft()
            cnt += 1
            l -= 1
        answer.append(cnt)
        cnt = 0

    return answer
