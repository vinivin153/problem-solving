def solution(citations):
    citations.sort(reverse=True)
    answer = len(citations)
    for i in range(len(citations)):
        if citations[i] < i + 1:
            answer = i
            break

    return answer
