import sys

n, k = map(int, sys.stdin.readline().split())

cnt = 0
while n != 1:
    if n < k:
        break
    if n % k == 0:
        n //= k
    else:
        n -= 1
    cnt += 1
cnt += n - 1

print(cnt)
