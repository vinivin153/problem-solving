import sys

input = sys.stdin.readline

s = input().rstrip()
q = int(input())
l = len(s) + 1

dp = [[0] * 27 for _ in range(l)]
for i in range(1, l):
    for j in range(1, 27):
        idx = ord(s[i - 1]) - 96
        dp[i][j] = dp[i - 1][j]
        if idx == j:
            dp[i][j] += 1


for _ in range(q):
    alpha, start, end = map(str, input().split())
    idx = ord(alpha) - 96
    print(dp[int(end) + 1][idx] - dp[int(start)][idx])
