import sys

input = sys.stdin.readline
n = int(input())
price = sorted([int(input()) for _ in range(n)], reverse=True)

ans = 0
for i in range(0, n, 3):
    ans += sum(price[i : i + 3])
    if i + 2 < n:
        ans -= price[i + 2]
print(ans)
