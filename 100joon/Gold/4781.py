import sys


input = sys.stdin.readline

while True:
    n, m = map(float, input().split())
    n = int(n)
    m = int(m * 100)
    if n == 0 and m == 0:
        break

    dp = [0] * (m + 1)
    cal = []
    price = []

    for _ in range(n):
        c, p = map(float, input().split())
        cal.append(int(c))
        price.append(int(round(p * 100, 0)))

    max_cal = 0
    for i in range(1, m + 1):
        for j in range(len(price)):
            if i - price[j] >= 0:
                max_cal = max(dp[i - price[j]] + cal[j], max_cal)
                dp[i] = max_cal

    print(max_cal)
