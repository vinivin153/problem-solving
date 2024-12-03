# 17:25 시작

import sys

input = sys.stdin.readline

k, n = map(int, input().split())
lines = sorted([int(input()) for _ in range(k)])

ans = 0
left, right = 1, lines[-1]
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for line in lines:
        cnt += line // mid

    if cnt >= n:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
