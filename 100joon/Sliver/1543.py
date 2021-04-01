import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

cnt = 0
start = 0
p = len(b)
while start < len(a):
    if b in a[start:]:
        start += a[start:].index(b) + p
        cnt += 1
        continue
    else:
        break

print(cnt)
