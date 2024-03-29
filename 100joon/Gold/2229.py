import sys

input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, n + 1):
    dp[i] = dp[i - 1]
    minv, maxv = arr[i], arr[i]
    for j in range(i - 1, 0, -1):
        if minv <= arr[j] <= maxv:
            continue

        minv = min(minv, arr[j])
        maxv = max(maxv, arr[j])
        dp[i] = max(dp[i], dp[j - 1] + maxv - minv)

print(dp[-1])
