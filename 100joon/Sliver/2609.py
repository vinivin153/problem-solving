from math import gcd

a, b = map(int, input().split())
x = gcd(a, b)
print(x)
print(a * b // x)
