import sys

n = int(input())

stat = []
visited = [0 for _ in range(n)]
for _ in range(n):
    stat.append(list(map(int, sys.stdin.readline().split())))

for i in range(n - 1):
    for j in range(i + 1, n):
        stat[i][j] += stat[j][i]


def dfs(idx, cnt):
    global result
    if cnt == n // 2:
        start = []
        link = []
        for i in range(n):
            if visited[i] == 1:
                start.append(i)
            else:
                link.append(i)
        start_stat = 0
        link_stat = 0
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                start_stat += stat[start[i]][start[j]]
                link_stat += stat[link[i]][link[j]]
        result = min(abs(start_stat - link_stat), result)
        if result == 0:
            print(result)
            sys.exit()

    for i in range(idx, n):
        if visited[i]:
            continue
        visited[i] = 1
        dfs(i + 1, cnt + 1)
        visited[i] = 0


result = sys.maxsize
dfs(0, 0)
print(result)
