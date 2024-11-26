n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
target = {}
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    target[(x, y)] = 0

t = list(target.keys())
sx, sy = t[0]
ex, ey = t[-1]
target[(sx, sy)] = True

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = 0
visited = [[False] * n for _ in range(n)]
visited[sx][sy] = True


def dfs(x, y, cnt):
    global ans
    if (x, y) == (ex, ey):
        k = list(target.values())
        for i in range(1, len(k) - 1):
            if not k[i] or k[i] >= k[i + 1]:
                break
        else:
            ans += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and not mat[nx][ny]:
                if (nx, ny) in target:
                    target[(nx, ny)] = cnt
                visited[nx][ny] = True
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = False
                if (nx, ny) in target:
                    target[(nx, ny)] = 0


dfs(sx, sy, 1)
print(ans)
