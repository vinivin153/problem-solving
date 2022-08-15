import sys

n, c = map(int, input().split())
arr = list(map(int, input().split()))

nums = {}

for i in arr:
    if i not in nums:
        nums[i] = 1
    else:
        nums[i] += 1

for i, j in sorted(nums.items(), key=lambda x: -x[1]):
    print((str(i) + " ") * j, end="")
