from collections import deque

n = int(input())
w = list(map(int, input().split()))

res = []


def dfs(val):
    if len(w) < 3:
        res.append(val)
        return

    for i in range(1, len(w) - 1):
        k = w[i - 1] * w[i + 1]
        tmp = w[i]
        del w[i]
        dfs(val + k)
        w.insert(i, tmp)


dfs(0)
print(max(res))
