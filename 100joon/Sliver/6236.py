import sys

input = sys.stdin.readline

n, m = map(int, input().split())
amount = [int(input()) for _ in range(n)]

left = max(amount)
right = 10**9
answer = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 1
    money = mid
    for i in amount:
        if money >= i:
            money -= i
            continue

        money = mid - i
        cnt += 1

    if cnt <= m:
        right = mid - 1
        answer = mid
    else:
        left = mid + 1

print(answer)
