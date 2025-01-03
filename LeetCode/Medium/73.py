class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        rset = set()
        cset = set()

        for i in range(n):
            for j in range(m):

                if not matrix[i][j]:
                    rset.add(i)
                    cset.add(j)
        
        for i in rset:
            for j in range(m):
                matrix[i][j] = 0

        for i in cset:
            for j in range(n):
                matrix[j][i] = 0