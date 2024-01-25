def solution(n):
    result = []
    while n:
        n -= 1
        m = n % 3
        if m == 0 or m == 1:
            m += 1
        elif m == 2:
            m = 4

        result.append(str(m))
        n //= 3

    return "".join(result[::-1])
