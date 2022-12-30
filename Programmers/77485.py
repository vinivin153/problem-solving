# 행렬 테두리 회전하기
def solution(rows, columns, queries):
    answer = []
    mat = [[columns * i + j + 1 for j in range(columns)] for i in range(rows)]

    def rotate(q):
        x1, y1, x2, y2 = q[0] - 1, q[1] - 1, q[2] - 1, q[3] - 1
        min_value = rows * columns

        # top
        temp1 = mat[x1][y2]
        for i in range(y2, y1, -1):
            if mat[x1][i] < min_value:
                min_value = mat[x1][i]
            mat[x1][i] = mat[x1][i - 1]

        # right
        temp2 = mat[x2][y2]
        for i in range(x2, x1, -1):
            if mat[i][y2] < min_value:
                min_value = mat[i][y2]
            mat[i][y2] = mat[i - 1][y2]

        # bottom
        temp3 = mat[x2][y1]
        for i in range(y1, y2):
            if mat[x2][i] < min_value:
                min_value = mat[x2][i]
            mat[x2][i] = mat[x2][i + 1]

        # left
        for i in range(x1, x2):
            if mat[i][y1] < min_value:
                min_value = mat[i][y1]
            mat[i][y1] = mat[i + 1][y1]

        mat[x1 + 1][y2] = temp1
        mat[x2][y2 - 1] = temp2
        mat[x2 - 1][y1] = temp3

        answer.append(min_value)

    for q in queries:
        rotate(q)

    return answer
