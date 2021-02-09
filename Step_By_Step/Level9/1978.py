import sys

input()
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
for i in a:
    if i == 1:
        continue
    elif i == 2:
        cnt += 1
    else:
        for j in range(2, i):
            if i % j == 0:
                break
        if j == i - 1:
            cnt += 1
print(cnt)
