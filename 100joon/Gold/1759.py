l, c = map(int, input().split())
alpha = list(map(str, input().split()))

alpha.sort()


def backtracking(v, key):
    if len(key) == l:
        cnt = 0
        for i in key:
            if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
                cnt += 1

        if cnt >= 1 and l - cnt >= 2:
            print("".join(key))
            return
        else:
            return

    for i in range(v, c):
        if visited[i] == 0:
            visited[i] = 1
            key.append(alpha[i])
            backtracking(i, key)
            visited[i] = 0
            key.pop()


visited = [0] * 15

backtracking(0, [])
