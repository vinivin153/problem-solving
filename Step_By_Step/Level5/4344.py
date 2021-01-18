import sys

size = int(sys.stdin.readline())
for i in range(size):
    a, *b = map(int, sys.stdin.readline().split())
    avg = sum(b) / a
    cnt = float(0)
    for j in range(a):
        if b[j] > avg:
            cnt += 1
    print("%.3f%%" % (cnt / a * 100))
