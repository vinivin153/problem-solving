import sys

input = sys.stdin.readline
str1 = [""] + list(input().rstrip())
str2 = [""] + list(input().rstrip())

l1, l2 = len(str1), len(str2)
dp = [[0] * l1 for _ in range(l2)]

ans = 0
for i in range(1, l2):
    for j in range(1, l1):
        if str1[j] == str2[i]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            ans = max(ans, dp[i][j])

print(ans)
