import heapq


def solution(ability, number):
    heap = []

    for a in ability:
        heapq.heappush(heap, a)

    for _ in range(number):
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        c = a + b

        heapq.heappush(heap, c)
        heapq.heappush(heap, c)

    return sum(heap)
