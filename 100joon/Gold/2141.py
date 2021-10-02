import sys

n = int(input())

loc = []
population = 0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    population += b
    loc.append([a, b])

loc.sort()

p = int(population / 2 + 0.5)
nums = 0
for i in range(n):
    nums += loc[i][1]
    if nums >= p:
        print(loc[i][0])
        break
