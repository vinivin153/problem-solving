import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    dp = [i for i in range(1, n + 1)]
    for i in range(1, k + 1):
        for j in range(n - 1, 0, -1):
            dp[j] = sum(dp[: j + 1])
    print(dp[-1])