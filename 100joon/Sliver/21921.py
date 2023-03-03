import sys

input = sys.stdin.readline

n, x = map(int, input().split())
visitor = list(map(int, input().split()))

max_visitor = sum(visitor[:x])
pre = max_visitor
cnt = 1
for i in range(x, n):
    pre = pre - visitor[i - x] + visitor[i]
    if pre > max_visitor:
        max_visitor = pre
        cnt = 1
    elif pre == max_visitor:
        cnt += 1

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(cnt)
