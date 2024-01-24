def solution(board):
    row, col = len(board), len(board[0])

    for r in range(1, row):
        for c in range(1, col):
            if board[r][c]:
                board[r][c] = (
                    min(board[r - 1][c - 1], board[r - 1][c], board[r][c - 1]) + 1
                )

    answer = 0
    for d in board:
        for i in d:
            if i > answer:
                answer = i

    return answer**2
