n, m = map(int, input().split())
tteok = list(map(int, input().split()))

result = 0


def bst(start, last):
    global result
    total = 0
    if start > last:
        return
    mid = (start + last) // 2
    for x in tteok:
        if x > mid:
            total = total + (x - mid)
    if total == m:
        result = mid
        return
    elif total < m:
        bst(start, mid - 1)
    else:
        result = mid
        bst(mid + 1, last)


bst(0, max(tteok))
print(result)
