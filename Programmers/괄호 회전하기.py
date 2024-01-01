from collections import deque


def solution(s):
    answer = 0
    queue = deque(s)
    for _ in range(len(s)):
        queue.rotate(1)
        stack = []

        for braket in queue:
            if braket in {"[", "{", "("}:
                stack.append(braket)
            elif stack and (
                (stack[-1] == "[" and braket == "]")
                or (stack[-1] == "{" and braket == "}")
                or (stack[-1] == "(" and braket == ")")
            ):
                stack.pop()
            else:
                break
        else:
            if not stack:
                answer += 1

    return answer
