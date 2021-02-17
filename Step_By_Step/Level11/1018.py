import sys

chess = []
board = []
for i in range(4):
    chess.append(["W", "B", "W", "B", "W", "B", "W", "B"])
    chess.append(["B", "W", "B", "W", "B", "W", "B", "W"])

n, m = map(int, input().split())
for _ in range(n):
    s = sys.stdin.readline()
    board.append(list(s[:-1]))

paint = 64
for i in range(n - 7):
    for j in range(m - 7):
        cnt = 0
        for row in range(8):
            for col in range(8):
                if board[row + i][col + j] != chess[row][col]:
                    cnt += 1
        paint = min(cnt, 64 - cnt, paint)

print(paint)