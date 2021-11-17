import sys

input = sys.stdin.readline

work = []
n = int(input())
for i in range(n):
    t, p = map(int, input().split())
    work.append([t, p])

work.insert(0, 0)

dp = [0] * 30

m = 0
for i in range(n, 0, -1):
    if work[i][0] + i <= n + 1:
        m = max(work[i][1] + dp[work[i][0] + i], m)
    dp[i] = m


print(max(dp))
