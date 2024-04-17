# Solution1
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())
# mat = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]


# dp = [[0] * (n + 1) for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         dp[i][j] = dp[i][j - 1] + mat[i][j]


# for _ in range(m):
#     ans = 0
#     x1, y1, x2, y2 = map(int, input().split())
#     for i in range(x1, x2 + 1):
#         ans += dp[i][y2] - dp[i][y1 - 1]

#     print(ans)


# Solution2
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]


dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i][j]

for _ in range(m):
    r1, c1, r2, c2 = map(int, input().split())
    print(dp[r2][c2] - dp[r2][c1 - 1] - dp[r1 - 1][c2] + dp[r1 - 1][c1 - 1])
