# 17:38 시작
# 17:58 저녁

import sys

input = sys.stdin.readline
n, c = map(int, input().split())
houses = sorted([int(input()) for _ in range(n)])

left, right = 1, houses[-1] - houses[0]
ans = 1
while left <= right:
    mid = (left + right) // 2
    prev = houses[0]
    cnt = 1

    for house in houses:
        if house - prev >= mid:
            cnt += 1
            prev = house

    if cnt >= c:
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
