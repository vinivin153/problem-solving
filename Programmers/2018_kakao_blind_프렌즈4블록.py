def solution(m, n, board):
    board = list(map(list, zip(*board)))
    dx = [0, 1, 1, 0]
    dy = [1, 0, 1, 0]
    answer = 0

    def find_square(x, y):
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if board[ny][nx] != board[y][x]:
                break
        else:
            erase.append([x, y])

    while True:
        erase = []

        # 2*2 찾기
        for i in range(m - 1):
            for j in range(n - 1):
                if board[j][i] != "0":
                    find_square(i, j)

        if not erase:
            return answer

        cols = set()
        # 2*2 지우기
        for x, y in erase:
            cols.add(y)
            cols.add(y + 1)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if board[ny][nx] != "0":
                    board[ny][nx] = "0"
                    answer += 1

        # 남은 블록 떨어지기
        for i in cols:
            stack = []
            for j in range(m):
                if board[i][j].isalpha():
                    stack.append(board[i][j])

            if stack:
                board[i] = ["0"] * (m - len(stack)) + stack
