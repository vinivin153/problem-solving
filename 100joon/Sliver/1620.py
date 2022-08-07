import sys

input = sys.stdin.readline

n, m = map(int, input().split())

poket_name = {}
poket_num = {}

for i in range(1, n + 1):
    name = input().rstrip()
    poket_name[name] = i
    poket_num[i] = name

for _ in range(m):
    q = input().rstrip()
    if q[0].isupper() or q[-1].isupper():
        print(poket_name[q])
    else:
        print(poket_num[int(q)])
