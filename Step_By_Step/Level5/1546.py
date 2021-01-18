import sys

size = int(input())
a = list(map(int, sys.stdin.readline().split()))
m = max(a)
for i in range(size):
    a[i] = a[i] / m * 100
print(sum(a) / size)
