def solution(n):
    if n == 1:
        return 1

    answer = 0
    visited = set()

    def backtracking(row):
        if row == n:
            nonlocal answer
            answer += 1
            return

        for col in range(n):
            for row2, col2 in visited:
                if col2 == col or row - row2 == abs(col - col2):
                    break
            else:
                visited.add((row, col))
                backtracking(row + 1)
                visited.remove((row, col))

    backtracking(0)
    return answer
