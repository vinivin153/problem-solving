import sys

n = int(input())

input = sys.stdin.readline
m, k = map(int, input().split())
a = sorted(list(map(int, input().split())), reverse=True)

v = m * k
for i in range(len(a)):
    v -= a[i]
    if v <= 0:
        print(i + 1)
        break
else:
    print("STRESS")
