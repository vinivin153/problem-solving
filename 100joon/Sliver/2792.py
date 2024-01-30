import sys

input = sys.stdin.readline
n, m = map(int, input().split())
jewel = [int(input()) for _ in range(m)]

left = 1
right = max(jewel)
result = 0
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for j in jewel:
        cnt += j // mid
        if j % mid:
            cnt += 1

    if cnt <= n:
        result = mid
        right = mid - 1
    else:
        left = mid + 1

print(result)
