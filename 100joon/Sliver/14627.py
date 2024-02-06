import sys

input = sys.stdin.readline

s, c = map(int, input().split())
p = [int(input()) for _ in range(s)]
answer = 0

left = 1
right = max(p)
while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for i in p:
        q, r = divmod(i, mid)
        cnt += q

    if cnt < c:
        right = mid - 1
    else:
        answer = mid
        left = mid + 1

print(sum(p) - answer * c)
