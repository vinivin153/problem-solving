def solution(sequence, k):
    value = sequence[0]
    start, end = 0, 0

    result = [0, 0]
    min_length = 10**9

    while start <= end:
        if value == k and min_length > (end - start + 1):
            min_length = end - start + 1
            result = [start, end]
        elif value > k:
            value -= sequence[start]
            start += 1
        else:
            end += 1
            if end >= len(sequence):
                break

            value += sequence[end]

    return result
