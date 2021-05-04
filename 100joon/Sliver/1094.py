import sys

x = int(sys.stdin.readline())

s = str(format(x, "b"))
print(s.count("1"))
