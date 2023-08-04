import sys

input = sys.stdin.readline
# C: 늘려야하는 수 N: 도시의 수
c, n = map(int, input().split())
dp = [sys.maxsize] * (c + 101)
dp[0] = 0
price = []
for _ in range(n):
    cost, customer = map(int, input().split())
    price.append([cost, customer])
    dp[customer] = cost

price.sort()

for i in range(1, c + 101):
    for cost, customer in price:
        if i - customer >= 0:
            if dp[i] > dp[i - customer] + cost:
                dp[i] = dp[i - customer] + cost
        else:
            break

print(min(dp[c:]))
