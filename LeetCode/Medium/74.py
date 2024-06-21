class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        x = -1
        left, right = 0, row - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] < target:
                x = mid
                left = mid + 1
            else:
                right = mid - 1

        if x == -1:
            return False

        left, right = 0, col - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[x][mid] == target:
                return True
            elif matrix[x][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
