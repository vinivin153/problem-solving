from collections import deque


def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append((0, 0))
    while queue:
        s, l = queue.popleft()
        if s == target and l == len(numbers):
            answer += 1
        if l == len(numbers):
            continue
        queue.append((s + numbers[l], l + 1))
        queue.append((s - numbers[l], l + 1))

    return answer
