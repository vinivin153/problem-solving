def solution(n):
    m = n + 1
    cnt = bin(n).count("1")

    while True:
        a = bin(m).count("1")
        if a == cnt:
            return m

        m += 1
