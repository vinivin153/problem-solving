def solution(n, left, right):
    answer = []
    for k in range(left, right + 1):
        i = k // n
        j = k % n
        if j <= i:
            answer.append(i + 1)
        else:
            answer.append(j + 1)

    return answer
