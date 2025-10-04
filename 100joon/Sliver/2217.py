import sys

input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]
ropes.sort()

max_value = 0
for i, rope in enumerate(ropes):
    max_value = max((n - i) * rope, max_value)

print(max_value)
