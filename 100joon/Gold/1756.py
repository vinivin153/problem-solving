import sys

input = sys.stdin.readline
d, n = map(int, input().split())
oven = list(map(int, input().split()))
pizza = list(map(int, input().split()))

for i in range(1, len(oven)):
    if oven[i] > oven[i - 1]:
        oven[i] = oven[i - 1]

pre = d
cnt = 0
for i in range(n):
    start = 0
    last = pre - 1
    check = False

    while start <= last:
        target = (start + last) // 2

        if oven[target] >= pizza[i]:
            start = target + 1
            pre = target
            check = True
        else:
            last = target - 1

    if check:
        cnt += 1

if cnt == n:
    print(pre + 1)
else:
    print(0)
