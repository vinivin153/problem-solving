import sys

n, m = map(int, sys.stdin.readline().split())

listen = set()
see = set()
unknown = []

for _ in range(n):
    listen.add((sys.stdin.readline().rstrip()))

for _ in range(m):
    see.add((sys.stdin.readline().rstrip()))

a = None
b = None
if n < m:
    a = listen
    b = see
else:
    b = listen
    a = see

cnt = 0
for i in a:
    if i in b:
        cnt += 1
        unknown.append(i)

print(cnt)
unknown.sort()
for i in unknown:
    print(i)

