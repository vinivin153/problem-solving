def solution(n):
    arr = []
    for i in range(1, n + 1):
        arr.append([-1] * i)

    r, c = -1, 0
    num = 1
    k = n
    while k >= 1:
        if k >= 1:
            for _ in range(k):
                r += 1
                arr[r][c] = num
                num += 1
            k -= 1

        if k >= 1:
            for _ in range(k):
                c += 1
                arr[r][c] = num
                num += 1
            k -= 1

        if k >= 1:
            for _ in range(k):
                c -= 1
                r -= 1
                arr[r][c] = num
                num += 1
            k -= 1

    return sum(arr, [])


solution(4)
