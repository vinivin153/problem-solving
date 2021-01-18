import sys

a = [0 for i in range(42)]

for i in range(10):
    a[int(sys.stdin.readline()) % 42] += 1
print(42 - a.count(0))