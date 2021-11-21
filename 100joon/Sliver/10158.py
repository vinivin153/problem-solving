import sys

w, h = map(int, sys.stdin.readline().split())
p, q = map(int, sys.stdin.readline().split())
t = int(input())


def cal(v, l):
    a = (t + v) // l
    check = a % 2
    b = (t + v) % l
    if check == 0:
        return b
    else:
        return l - b


x = cal(p, w)
y = cal(q, h)
print(x, y)
