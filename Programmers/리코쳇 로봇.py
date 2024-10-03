from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(board):
    mat = [list(b) for b in board]
    n, m = len(board), len(board[0])

    start = (0, 0)
    target = (0, 0)
    for i in range(n):
        for j in range(m):
            if mat[i][j] == "R":
                start = (i, j)

            if mat[i][j] == "G":
                target = (i, j)

    print(start, target)

    def move(x1, y1, x2, y2):
        x = x1 + x2
        y = y1 + y2

        while (0 <= x < n and 0 <= y < m) and mat[x][y] != "D":
            x += x2
            y += y2

        return (x - x2, y - y2)

    queue = deque()
    queue.append((start[0], start[1], 0))
    visited = set()
    visited.add(start)
    while queue:
        x, y, cnt = queue.popleft()

        if mat[x][y] == "G":
            return cnt

        for i in range(4):
            nx, ny = move(x, y, dx[i], dy[i])
            if (nx, ny) not in visited:
                queue.append((nx, ny, cnt + 1))
                visited.add((nx, ny))

    return -1
