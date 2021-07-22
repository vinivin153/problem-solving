n = int(input())
parts = list(map(int, input().split()))
m = int(input())
needs = list(map(int, input().split()))

parts.sort()


def bst(start, last, target):
    if start > last:
        print("no", end=" ")
        return
    mid = (start + last) // 2
    if parts[mid] == target:
        print("yes", end=" ")
    else:
        if target < parts[mid]:
            bst(start, mid - 1, target)
        else:
            bst(mid + 1, last, target)


for need in needs:
    bst(0, n - 1, need)
