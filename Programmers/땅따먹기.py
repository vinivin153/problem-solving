def solution(land):
    dp = land[0]

    for row in range(1, len(land)):
        temp = [0] * 4
        for col in range(4):
            temp[col] = max(dp[:col] + dp[col + 1 :]) + land[row][col]

        dp = temp

    return max(dp)
