def solution(targets):
    targets.sort(key=lambda x: (x[0], x[1]))

    answer = 0
    i = 1
    end = targets[0][1]

    while i < len(targets):
        if end <= targets[i][0]:
            answer += 1
            end = targets[i][1]
        else:
            if targets[i][1] < end:
                end = targets[i][1]

        i += 1

    return answer + 1
