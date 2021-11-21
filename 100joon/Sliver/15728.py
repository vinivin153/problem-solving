import sys

input = sys.stdin.readline

n, k = map(int, input().split())
share = sorted(list(map(int, input().split())))
team = sorted(list(map(int, input().split())))

result = []
for t in team:
    if t > 0:
        result.append(t * share[-1])
    else:
        result.append(t * share[0])

result.sort()
print(result[-(k + 1)])
