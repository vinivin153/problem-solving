def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for time in range(len(prices)):
        while stack and prices[stack[-1]] > prices[time]:
            k = stack.pop()
            answer[k] = time - k

        stack.append(time)

    for i in stack:
        answer[i] = time - i

    return answer
