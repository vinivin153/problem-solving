import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
wok = list(map(int, input().split()))

dp = [sys.maxsize] * (n + 1)


for i in combinations(wok, 2):
    k = sum(i)
    if k <= n:
        wok.append(sum(i))

wok.sort()

for i in wok:
    dp[i] = 1

for i in range(1, n + 1):
    for j in wok:
        if i - j > 0:
            if dp[i] > dp[i - j] + 1:
                dp[i] = dp[i - j] + 1
        else:
            break

if dp[n] == sys.maxsize:
    print(-1)
else:
    print(dp[n])
