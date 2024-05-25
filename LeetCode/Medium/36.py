class Solution:
    def is_duplicate(self, arr):
        nums = set()
        for num in arr:
            if num.isdigit():
                if num not in nums:
                    nums.add(num)
                else:
                    return True

        return False

    def isValidSudoku(self, board):
        for row in board:
            if self.is_duplicate(row):
                return False

        for col in zip(*board):
            if self.is_duplicate(col):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = set()
                for r in range(3):
                    for c in range(3):
                        x, y = i + r, j + c
                        if board[x][y].isdigit():
                            if board[x][y] not in nums:
                                nums.add(board[x][y])
                            else:
                                return False

        return True
