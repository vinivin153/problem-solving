import sys

x, y = map(int, input().split())
z = (100 * y) // x

if z == 99:
    print(-1)
    sys.exit()

answer = -1
left = 1
right = x

while left <= right:
    mid = (left + right) // 2

    k = 100 * (y + mid) // (x + mid)
    if z == k:
        left = mid + 1
    else:
        right = mid - 1
        answer = mid

print(answer)
