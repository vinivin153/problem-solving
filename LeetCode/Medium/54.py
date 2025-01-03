class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:        
        ans = []
        x, y = 0, -1
        rd, cd = 1, 1
        row_size, col_size = len(mat), len(mat[0])
        while row_size and col_size:
            # 가로로 이동
            for i in range(col_size):
                y += cd
                ans.append(mat[x][y])
            col_size -= 1
            cd *= -1

            # 세로로 이동
            for i in range(1, row_size):
                x += rd
                ans.append(mat[x][y])
            row_size -= 1
            rd *= -1

        return ans