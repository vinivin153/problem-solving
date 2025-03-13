import sys

input = sys.stdin.readline
n, m = map(int, input().split())

mat = [[False] * m ]
visited = [ [False] * m for _ in range(n)]

dx = [-1, -1, 0]
dy = [0, -1, -1]
ans = 0

def isValidScope(x, y):
    return 0 <= x < n and 0 <= y < m


def isNemo(x, y):
    for i in range(3):
        nx = x + dx[i]
        ny = y + dy[i]
        if isValidScope(nx, ny):
            if not visited[nx][ny]:
                return False
        else:
            return False
        
    return True

        

def dfs(x, y, d):
    global ans
    ans += 1
    k = y
    for i in range(x, n):
        if i != x: k = 0
        for j in range(k, m):
            if not isNemo(i, j):
                visited[i][j] = True
                dfs(i, j + 1, d + 1)
                visited[i][j] = False

dfs(0, 0, 0)
print(ans)