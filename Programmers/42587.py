# 스택/큐 프린터

from collections import deque


def solution(priorities, location):
    p = sorted(priorities, reverse=True)
    priorities = enumerate(priorities)
    queue = deque(priorities)
    p_idx = 0
    cnt = 0
    while queue:
        idx, x = queue.popleft()
        if x == p[p_idx]:
            cnt += 1
            p_idx += 1
            if location == idx:
                return cnt
        else:
            queue.append((idx, x))


solution([1, 1, 9, 1, 1, 1], 0)
