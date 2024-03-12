a = int(input())
b = int(input())

prime_num = set([2, 3, 5, 7, 11, 13, 17])

dp = [[19 * [0] for _ in range(19)] for _ in range(19)]

a_win = a * 0.01 * (100 - b) * 0.01
b_win = (100 - a) * 0.01 * b * 0.01
draw_goal = a * 0.01 * b * 0.01
draw_nogoal = (100 - a) * 0.01 * (100 - b) * 0.01

dp[0][0][0] = 1


for i in range(1, 19):
    for a in range(0, 19):
        for b in range(0, 19):
            if a > 0:
                dp[i][a][b] += dp[i - 1][a - 1][b] * a_win
            if b > 0:
                dp[i][a][b] += dp[i - 1][a][b - 1] * b_win
            if a and b:
                dp[i][a][b] += dp[i - 1][a - 1][b - 1] * draw_goal
            dp[i][a][b] += dp[i - 1][a][b] * draw_nogoal


ans = 0
for i in range(19):
    for j in range(19):
        if i in prime_num or j in prime_num:
            ans += dp[18][i][j]
print(ans)
