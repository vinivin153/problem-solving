import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(alph, x, y):
    stack = []
    stack.append((x, y, visited[x][y]))
    while stack:
        x, y, z = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = z + 1
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == alph:
                if visited[nx][ny] == 0:
                    stack.append((nx, ny, visited[x][y] + 1))
                elif visited[x][y] - visited[nx][ny] >= 3:
                    return 1
    return 0


for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:
            if dfs(mat[i][j], i, j):
                print("Yes")
                exit()

print("No")
