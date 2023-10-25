import math


def dfs(gen, idx):
    if gen == 1:
        return "Rr"

    parent = dfs(gen - 1, (idx - 1) // 4 + 1)

    if parent == "RR" or parent == "rr":
        return parent

    res = (idx - 1) % 4

    if res == 0:
        return "RR"
    if res == 3:
        return "rr"

    return "Rr"


def solution(queries):
    answer = []

    for query in queries:
        n, p = query
        answer.append(dfs(n, p))

    return answer
