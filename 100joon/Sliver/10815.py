def bs(start, end, target):
    mid = int((start + end) / 2)
    if start > end:
        print(0, end=" ")
        return
    if target == arr[mid]:
        print(1, end=" ")
        return
    elif arr[mid] > target:
        bs(start, mid - 1, target)
    else:
        bs(mid + 1, end, target)


n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split()))

for i in range(m):
    bs(0, n - 1, arr2[i])
