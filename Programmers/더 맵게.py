from heapq import heappush, heappop, heapify


def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville[0] < K and len(scoville) >= 2:
        answer += 1
        heappush(scoville, heappop(scoville) + heappop(scoville) * 2)

    if scoville[0] < K:
        return -1

    return answer
