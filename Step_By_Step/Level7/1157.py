s = list(input().upper())
a = [0 for _ in range(26)]
for i in s:
    a[ord(i) - 65] += 1
m = max(a)
if a.count(m) == 1:
    print(chr(65 + a.index(m)))
else:
    print("?")