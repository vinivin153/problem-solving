from itertools import combinations


n = int(input())
ans = []
flag = False

for i in range(1, n + 1):
    num, t = map(str, input().split())
    t = int(t)
    num = list(num)
    ans = []
    coms = []
    flag = False
    for com in combinations(range(len(num)), 2):
        coms.append(com)

    max_num = sorted(num, reverse=True)

    def backtracking(cnt, value):
        global ans, flag
        if cnt == t:
            if ans < value:
                ans = value[:]
            return

        if value == max_num and 0 < cnt < t:
            if (t - cnt) % 2 == 1:
                if len(set(value)) == len(value):
                    value[-1], value[-2] = value[-2], value[-1]
            ans = value[:]
            flag = True
            return

        for a, b in coms:
            if flag:
                return

            value[a], value[b] = value[b], value[a]
            backtracking(cnt + 1, value)
            value[a], value[b] = value[b], value[a]

    backtracking(0, num)
    ans = int("".join(ans))
    print(f"#{i} {ans}")
