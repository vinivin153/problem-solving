import sys

input = sys.stdin.readline

n, m = map(int, input().split())
st = list(map(int, input().split()))

ans = -1
start = 0
last = 1000000 * 1000000

while start <= last:
    mid = (start + last) // 2
    cnt = 0

    for i in st:
        cnt += mid // i

    if cnt >= m:
        ans = mid
        last = mid - 1
    else:
        start = mid + 1

print(ans)
