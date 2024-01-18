def solution(arr):
    n = max(arr)
    m = n
    while True:
        for i in arr:
            if m % i:
                break
        else:
            return m

        m += n
