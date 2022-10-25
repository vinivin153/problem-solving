# 출석부
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input().split()))


arr.sort(key=lambda x: (x[0], x[1]))
print(*arr[k - 1])
