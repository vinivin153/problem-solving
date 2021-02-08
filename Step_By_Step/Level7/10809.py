import sys

a = sys.stdin.readline()
for i in range(26):
    print(a.find(chr(i + 97)), end=" ")
