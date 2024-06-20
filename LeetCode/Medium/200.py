from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])

        visited = [[False] * col for _ in range(row)]

        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]

        def bfs(i, j):
            visited[i][j] = True
            queue = deque()
            queue.append((i, j))
            while queue:
                x, y = queue.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < row and 0 <= ny < col:
                        if not visited[nx][ny] and grid[nx][ny] == "1":
                            visited[nx][ny] = True
                            queue.append([nx, ny])

        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and not visited[i][j]:
                    ans += 1
                    bfs(i, j)

        return ans
