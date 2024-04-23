s1 = input().rstrip()
s2 = input().rstrip()

l1, l2 = len(s1) + 1, len(s2) + 1

dp = [[0] * l2 for _ in range(l1)]

for i in range(1, l1):
    for j in range(1, l2):
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if s1[i - 1] == s2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1


print(dp[l1 - 1][l2 - 1])
