n, k = map(int, input().split())

ans = "NO"
rowleft, rowright = 0, n // 2 + 1
while rowleft <= rowright:
    mid = (rowleft + rowright) // 2
    res = (mid + 1) * (n - mid + 1)
    if k == res:
        ans = "YES"
        break

    if res > k:
        rowright = mid - 1
    else:
        rowleft = mid + 1


print(ans)
