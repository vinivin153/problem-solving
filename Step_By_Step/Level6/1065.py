import sys

num = int(sys.stdin.readline())
count = 0


def hansu(n):
    global count
    if n < 100:
        count += 1
        return
    else:
        a = n // 100
        b = n // 10 % 10
        c = n % 10
        if a - b == b - c:
            count += 1


for i in range(1, num + 1):
    hansu(i)
print(count)
