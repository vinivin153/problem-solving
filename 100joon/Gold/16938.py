import sys

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
problems = sorted(list(map(int, input().split())))

ans = 0
visited = [False] * n
min_level = 10**9


def dfs(sum_level, max_level, cnt, k):
    global min_level, ans
    if cnt >= 2:
        if l <= sum_level <= r and max_level - min_level >= x:
            ans += 1
        elif sum_level > r:
            return

    for i in range(k, n):
        if not visited[i]:
            visited[i] = True
            if cnt == 0:
                min_level = problems[i]
            dfs(sum_level + problems[i], problems[i], cnt + 1, i + 1)
            visited[i] = False


dfs(0, 0, 0, 0)
print(ans)
