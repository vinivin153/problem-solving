import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
prefixsum1 = nums[:]
prefixsum2 = nums[::-1]

for i in range(1, n):
    prefixsum1[i] += prefixsum1[i - 1]
    prefixsum2[i] += prefixsum2[i - 1]

prefixsum2 = prefixsum2[::-1]

res = 0
for i in range(1, n - 1):
    max_value1 = prefixsum1[i] - prefixsum1[0] + prefixsum2[i] - prefixsum2[-1]
    max_value2 = prefixsum1[-1] - nums[0] - nums[i] + prefixsum1[-1] - prefixsum1[i]
    max_value3 = prefixsum1[-1] - nums[-1] - nums[i] + prefixsum1[-1] - prefixsum2[i]

    max_value = max(max_value1, max_value2, max_value3)

    if max_value > res:
        res = max_value


print(res)
