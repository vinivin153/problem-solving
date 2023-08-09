import sys

input = sys.stdin.readline


n = int(input())
m = int(input())
vip = []
for _ in range(m):
    vip.append(int(input()))

memo = [0] * 41
memo[0] = 1
memo[1] = 1
memo[2] = 2
for i in range(3, 41):
    memo[i] = memo[i - 1] + memo[i - 2]

if m == 0:
    print(memo[n])
    sys.exit()

res = 1
pre = 0
for i in vip:
    res *= memo[i - pre - 1]
    pre = i

if vip[-1] != n:
    res *= memo[n - pre]

print(res or 1)
