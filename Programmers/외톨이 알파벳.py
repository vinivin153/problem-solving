def solution(input_string):
    visited = set()
    answer = set()
    for i in range(len(input_string) - 1):
        if input_string[i] not in visited:
            if input_string[i + 1] == input_string[i]:
                continue
            else:
                visited.add(input_string[i])
        else:
            if input_string[i] not in answer:
                answer.add(input_string[i])

    if input_string[-1] in visited and input_string[-1] not in answer:
        answer.add(input_string[-1])

    s = sorted(answer)

    if not s:
        return "N"
    else:
        return "".join(s)
