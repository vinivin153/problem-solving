import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)

cnt = 0
for coin in coins:
    if k >= coin:
        cnt += k // coin
        k %= coin
    else:
        continue

    if k == 0:
        print(cnt)
        break
