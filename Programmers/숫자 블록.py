from collections import deque


def divisor(n):
    result = deque([1])
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            result.appendleft(i)
            if n // i <= 10**7:
                result.append(n // i)

    return max(result)


def solution(begin, end):
    answer = []

    for num in range(begin, end + 1):
        answer.append(divisor(num))

    if begin == 1:
        answer[0] = 0

    return answer
