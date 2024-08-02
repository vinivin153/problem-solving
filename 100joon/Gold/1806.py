import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum1 = arr[0]
ans = 10**8

while True:
    if sum1 >= s:
        ans = min(ans, end - start + 1)
        sum1 -= arr[start]
        start += 1
    else:
        end += 1
        if end == n:
            break
        sum1 += arr[end]

if ans == 10**8:
    print(0)
else:
    print(ans)
