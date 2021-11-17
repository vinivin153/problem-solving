import sys


input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))


def bst(start, end, target):
    if start > end:
        print(0)
        return
    mid = (start + end) // 2
    if a[mid] == target:
        print(1)
        return

    if target < a[mid]:
        bst(start, mid - 1, num)
    else:
        bst(mid + 1, end, num)


for num in b:
    bst(0, n - 1, num)
