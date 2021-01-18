import sys

cnt = 1
m = int(sys.stdin.readline())
for i in range(2, 10):
    if (a := int(sys.stdin.readline())) > m:
        m = a
        cnt = i
print(m, cnt, sep="\n")