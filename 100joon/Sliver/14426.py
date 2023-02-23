import sys

input = sys.stdin.readline

n, m = map(int, input().split())
s = []
prefix = []
for _ in range(n):
    s.append(input().rstrip())

for _ in range(m):
    prefix.append(input().rstrip())

s.sort()
prefix.sort()

s1 = 0
s2 = 0

ans = 0
while s1 < m and s2 < n:
    if prefix[s1][0] > s[s2][0]:
        s2 += 1
    elif prefix[s1][0] < s[s2][0]:
        s1 += 1
    elif prefix[s1][0] == s[s2][0]:
        t = len(prefix[s1])
        if s[s2][:t] == prefix[s1]:
            ans += 1
            s1 += 1
        elif prefix[s1] > s[s2][:t]:
            s2 += 1
        else:
            s1 += 1
print(ans)
