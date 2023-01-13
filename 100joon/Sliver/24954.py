import sys

input = sys.stdin.readline

n = int(input())
cost = [0] + list(map(int, input().split()))
event = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    k = int(input())
    for _ in range(k):
        event[i].append(list(map(int, input().split())))

ans = 10 ** 5
visited = [False] * (n + 1)


def dfs(cnt, total):
    global cost, ans
    if cnt == n:
        if ans > total:
            ans = total
        return

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            temp = cost[:]
            for j, c in event[i]:
                cost[j] = max(cost[j] - c, 1)
            dfs(cnt + 1, total + cost[i])
            cost = temp
            visited[i] = False


dfs(0, 0)
print(ans)
