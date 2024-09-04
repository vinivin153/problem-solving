import sys

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
start = []
for _ in range(m):
    x, y = map(int, input().split())
    start.append([x - 1, y - 1])


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * n for _ in range(n)]
ans = 0
for x, y in start:
    ans += mat[x][y]
    visited[x][y] = True


# 현재 좌표, 친구번호, 해당 친구의 이동횟수, 총합
def backtracking(pos, idx, cnt, value):
    global ans
    if idx == m - 1 and cnt == 3:
        ans = max(ans, value)
        return

    if cnt == 3:
        backtracking(start[idx + 1], idx + 1, 0, value)
        return

    x, y = pos
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                backtracking((nx, ny), idx, cnt + 1, value + mat[nx][ny])
                visited[nx][ny] = False


backtracking(start[0], 0, 0, ans)
print(ans)
