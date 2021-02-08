import sys

n = int(sys.stdin.readline())
for i in range(n):
    num, arr = map(list, sys.stdin.readline().split())
    for j in range(len(arr)):
        print(arr[j] * int(num[0]), end="")
    print()
