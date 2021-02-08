import sys

num = int(input())
result = 0
for _ in range(num):
    cnt = 0
    s = list(sys.stdin.readline())
    for i in range(len(s) - 2):
        if s[i] != s[i + 1]:
            cnt += 1
    if (cnt + 1) == (len(set(s)) - 1):
        result += 1
print(result)
