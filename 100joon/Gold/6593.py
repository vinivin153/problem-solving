import sys
from collections import deque

input = sys.stdin.readline


while True:
    l, r, c = map(int, input().split())
    if [l, r, c] == [0, 0, 0]:
        break

    mat = []
    for _ in range(l):
        k = [list(input().rstrip()) for _ in range(r)]
        input()
        mat.append(k)

    def game():
        for z in range(l):
            for x in range(c):
                for y in range(r):
                    if mat[z][x][y] == "S":
                        bfs(z, x, y)
                        return

    dx = [0, 0, -1, 1, 0, 0]
    dy = [-1, 1, 0, 0, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    def bfs(z, x, y):
        queue = deque()
        queue.append((z, x, y, 0))
        while queue:
            z, x, y, cnt = queue.popleft()
            if mat[z][x][y] == "E":
                print(f"Escaped in {cnt} minute(s).")
                return
            for i in range(6):
                nx = dx[i] + x
                ny = dy[i] + y
                nz = dz[i] + z
                if 0 <= nz < l and 0 <= nx < r and 0 <= ny < c:
                    if mat[nz][nx][ny] == ".":
                        queue.append((nz, nx, ny, cnt + 1))
                        mat[nz][nx][ny] = "X"
                    elif mat[nz][nx][ny] == "E":
                        queue.append((nz, nx, ny, cnt + 1))
        print("Trapped!")

    game()
