import sys

n, m = map(int, sys.stdin.readline().split())

max_card = 0
for i in range(n):
    card = list(map(int, sys.stdin.readline().split()))
    max_card = max(max_card, min(card))

print(max_card)
