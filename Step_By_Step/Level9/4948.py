import sys


def pNumber(n: int):
    s = int((n * 2) ** 0.5) + 1
    a = [False, False] + [True] * (n * 2 - 1)
    for i in range(2, s + 1):
        if a[i] == True:
            for j in range(i + i, n * 2 + 1, i):
                a[j] = False
    return a


a = []
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        a.append(n)

s = pNumber(max(a))

for i in a:
    count = 0
    for j in range(i + 1, i * 2 + 1):
        if s[j] == True:
            count += 1
    print(count)