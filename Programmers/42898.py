# 등굣길


def solution(m, n, puddles):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    dp[1][0] = 1

    check = set()
    for i, j in puddles:
        check.add((i, j))

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (i, j) in check:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007

    return dp[m][n]


print(solution(4, 3, [[2, 2]]))
