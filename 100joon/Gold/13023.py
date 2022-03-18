import sys

input = sys.stdin.readline


def dfs(x):
    stack = []
    stack.append((x, set(), 1))
    while stack:
        x, visited, cnt = stack.pop()
        if cnt == 5:
            print(1)
            sys.exit(0)
        for friend in friends[x]:
            if friend not in visited:
                stack.append((friend, visited.union({x}), cnt + 1))


n, m = map(int, input().split())
friends = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

for i in range(1, n):
    dfs(i)

print(0)
