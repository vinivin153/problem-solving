import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
dp = [1000] * n

dp[0] = 0
for i in range(1, n):
    if arr[i] == 0:
        continue
    for j in range(1, 100):
        if i - j >= 0:
            if arr[i - j] >= j:
                dp[i] = min(dp[i], dp[i - j]) + 1

if dp[n - 1] == 1000:
    print(-1)
else:
    print(dp[n - 1])
