def base_convert(n, x):
    alpha = ["A", "B", "C", "D", "E", "F"]
    result = ""
    while x:
        k = x % n

        if k >= 10:
            k = alpha[k - 10]

        result = str(k) + result
        x //= n

    return result


def solution(n, t, m, p):
    num = 1
    s = "0"
    while len(s) < m * t:
        k = base_convert(n, num)
        s += k
        num += 1

    answer = ""
    for i in range(p - 1, m * t, m):
        answer += s[i]

    return answer
