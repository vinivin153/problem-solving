def solution(sizes):
    for size in sizes:
        if size[0] < size[1]:
            size[0], size[1] = size[1], size[0]

    answer = max(sizes)[0] * max(sizes, key=lambda x: x[1])[1]
    return answer
