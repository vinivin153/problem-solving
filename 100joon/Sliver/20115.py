import sys

input = sys.stdin.readline
n = int(input())
drinks = list(map(int, input().split()))

drinks.sort(reverse=True)
while len(drinks) > 1:
    x = drinks.pop()
    drinks[0] += x / 2

print(drinks[0])
