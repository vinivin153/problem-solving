from collections import deque


def solution(n, m, hole):
    ans = 0
    s = set()
    for h in hole:
        a, b = h
        s.add((a - 1, b - 1))
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 0
    queue = deque()
    queue.append((0, 0, 0))
    while queue:
        x, y, used = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][used]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if (nx, ny) not in s:
                    if not visited[nx][ny][used]:
                        visited[nx][ny][used] = visited[x][y][used] + 1
                        queue.append((nx, ny, used))
            if not used:
                nx += dx[i]
                ny += dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in s:
                        if not visited[nx][ny][1]:
                            visited[nx][ny][1] = visited[x][y][0] + 1
                            queue.append((nx, ny, 1))
    return -1
