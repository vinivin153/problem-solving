import math

n = int(input())

trees = [int(input()) for _ in range(n)]

diff = trees[1] - trees[0]
for i in range(1, n - 1):
    diff = math.gcd(diff, trees[i + 1] - trees[i])


print((trees[-1] - trees[0]) // diff + 1 - n)
