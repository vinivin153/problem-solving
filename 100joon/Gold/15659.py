import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
nums = list(map(str, input().split()))
calc = ["+", "-", "*", "//"]
func = []
for idx, value in enumerate(list(map(int, input().split()))):
    func += [calc[idx]] * value

per = set()
for p in permutations(func, n - 1):
    per.add(p)

INF = sys.maxsize
min_value = INF
max_value = -1 * INF

for p in per:
    exp = ""
    for j in range(n - 1):
        exp += nums[j] + p[j]
    exp += nums[-1]
    result = eval(exp)
    max_value = max(max_value, result)
    min_value = min(min_value, result)


print(max_value)
print(min_value)
