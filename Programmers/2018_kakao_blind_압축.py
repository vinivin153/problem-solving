def solution(msg):
    d = {chr(65 + i): i + 1 for i in range(26)}
    idx = 27
    s = msg[0]
    answer = []

    for i in range(len(msg) - 1):
        if s + msg[i + 1] in d:
            s += msg[i + 1]
        else:
            answer.append(d[s])
            d[s + msg[i + 1]] = idx
            idx += 1
            s = msg[i + 1]

    answer.append(d[s])

    return answer
