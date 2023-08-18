import sys

input = sys.stdin.readline

n, k = map(int, input().split())
kit = list(map(int, input().split()))

visited = [False] * (n + 1)
ans = 0


def backtracking(weight, cnt):
    global ans
    if weight < 500:
        return
    elif cnt == n:
        ans += 1
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtracking(weight + kit[i] - k, cnt + 1)
            visited[i] = False


backtracking(500, 0)
print(ans)
