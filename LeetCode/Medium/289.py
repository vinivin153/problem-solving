class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        n, m = len(board), len(board[0])

        dx = [-1, -1, -1, 0, 0 , 1, 1, 1]
        dy = [-1, 0, 1, -1, 1, -1, 0, 1]

        new_board = [[0] * m for _ in range(n)]

        def next_gen(x, y):
            lives = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m:
                    if board[nx][ny]:
                        lives += 1
            
            if (board[x][y] == 1 and 2 <= lives <= 3) or (board[x][y] == 0 and lives == 3):
                new_board[x][y] = 1


        for i in range(n):
            for j in range(m):
                next_gen(i, j)
        
        for i in range(n):
            for j in range(m):
                board[i][j] = new_board[i][j]