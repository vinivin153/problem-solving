from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])
    visited = [[False] * m for _ in range(n)]
    memo = [0] * m

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def bfs(x, y):
        cnt = 1
        check.add(y)
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and land[nx][ny] == 1:
                        visited[nx][ny] = True
                        cnt += 1
                        check.add(ny)
                        queue.append((nx, ny))
        return cnt

    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j]:
                visited[i][j] = True
                check = set()
                res = bfs(i, j)
                for c in check:
                    memo[c] += res
    print(memo)
    return max(memo)
