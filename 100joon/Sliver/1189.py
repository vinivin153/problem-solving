import sys

input = sys.stdin.readline
r, c, k = map(int, input().split())
mat = [list(input().rstrip()) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited[r - 1][0] = True


def backTracking(cnt, x, y):
    global ans
    if x == 0 and y == c - 1 and cnt == k:
        ans += 1
        return

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < r and 0 <= ny < c:
            if visited[nx][ny] == 0 and mat[nx][ny] == ".":
                visited[nx][ny] = True
                backTracking(cnt + 1, nx, ny)
                visited[nx][ny] = False


backTracking(1, r - 1, 0)
print(ans)
