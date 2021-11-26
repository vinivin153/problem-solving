import sys

input = sys.stdin.readline


t = int(input())
for i in range(t):
    money = int(input())
    q = money // 25
    money = money % 25
    d = money // 10
    money = money % 10
    n = money // 5
    p = money % 5
    print(q, d, n, p)
