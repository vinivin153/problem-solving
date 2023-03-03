import sys

input = sys.stdin.readline

n = int(input())
request = list(map(int, input().split()))
budget = int(input())

start = 1
end = max(request)
while start <= end:
    res = 0
    mid = (start + end) // 2

    for r in request:
        if mid > r:
            res += r
        else:
            res += mid

    if res > budget:
        end = mid - 1
    elif res < budget:
        start = mid + 1
    else:
        print(mid)
        break
else:
    print(end)
