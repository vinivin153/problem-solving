import sys


def pNumber(n):
    for i in range(2, int(n ** 0.5) + 1):
        if s[i] == 1:
            for j in range(i + i, n + 1, i):
                s[j] = 0


n = 10000
s = [0, 0] + [1] * (10000 - 1)
pNumber(n)

t = int(input())
for i in range(t):
    m = int(sys.stdin.readline())
    for j in range(m // 2, n + 1):
        if s[m - j] == 1 and s[j] == 1:
            print(m - j, j)
            break
