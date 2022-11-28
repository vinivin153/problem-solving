# 제곱암호
import sys

input = sys.stdin.readline
n = int(input())
s = input().rstrip()
ans = ""
for i in range(0, n, 2):
    t = ord(s[i]) + ((int(s[i + 1]) ** 2) % 26)
    if t > 122:
        t -= 26
    ans += chr(t)
print(ans)
