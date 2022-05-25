dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def inputNumber(mat, num, size, x, y):
    stack = []
    stack.append((x, y))
    mat[x][y] = num
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < size and 0 <= ny < size:
                if mat[nx][ny] == 1:
                    stack.append((nx, ny))
                    mat[nx][ny] = num


def outputPosition(mat, visit, size, x, y, flag):
    position = set()
    position.add((0, 0))
    a, b = -x, -y
    stack = []
    stack.append((x, y))
    visit[x][y] = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < size and 0 <= ny < size:
                if visit[nx][ny] == 0 and (mat[nx][ny] ^ flag):
                    stack.append((nx, ny))
                    visit[nx][ny] = 1
                    position.add((nx + a, ny + b))
    return position


def rotate(mat, size):
    tmp = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            tmp[j][size - i - 1] = mat[i][j]

    return tmp


def solution(game_board, table):
    n = len(game_board)
    num = 2
    pos = []
    visited = set()
    visit = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                inputNumber(table, num, n, i, j)
                num += 1

            if visit[i][j] == 0 and game_board[i][j] == 0:
                pos.append(outputPosition(game_board, visit, n, i, j, 1))

    pos2 = [[] for _ in range(num)]
    for _ in range(4):
        visit = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visit[i][j] == 0 and table[i][j] > 0:
                    pos2[table[i][j]].append(outputPosition(table, visit, n, i, j, 0))
        table = rotate(table, n)

    answer = 0
    for i in range(2, num):
        for j in range(len(pos)):
            if pos[j] in pos2[i] and i not in visited:
                answer += len(pos[j])
                visited.add(i)
                pos.remove(pos[j])
                break

    return answer
