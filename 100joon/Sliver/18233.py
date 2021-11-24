import sys

n, p, e = map(int, input().split())
members = [list(map(int, input().split())) for _ in range(n)]
result = [0] * n
visited = [0] * n
idx = []


def backtracking(v, a, b, cnt):
    if cnt == p:
        if a <= e <= b:
            for i in idx:
                result[i] = members[i][0]

            k = sum(result)
            if k == e:
                print(*result)
                exit()
            else:
                k = e - k
                for i in idx:
                    if k > members[i][1] - members[i][0]:
                        result[i] = members[i][1]
                        k = k - (members[i][1] - members[i][0])
                    else:
                        result[i] += k
                        print(*result)
                        exit()
        else:
            return

    for i in range(v, n):
        if visited[i] == 0:
            idx.append(i)
            visited[i] = 1
            backtracking(i + 1, a + members[i][0], b + members[i][1], cnt + 1)
            idx.pop()
            visited[i] = 0


backtracking(0, 0, 0, 0)

print(-1)
