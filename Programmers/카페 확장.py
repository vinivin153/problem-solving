from collections import deque


def solution(menu, order, k):
    answer = 0
    queue = deque()
    now_time = 0
    for i in range(len(order)):
        now_time += k

        while queue and queue[0] <= now_time:
            queue.popleft()

        if not queue:
            queue.append(now_time + menu[order[i]])
        else:
            queue.append(queue[-1] + menu[order[i]])

        answer = max(answer, len(queue))

    return answer
