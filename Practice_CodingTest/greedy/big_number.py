import sys

n, m, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

a = max(nums)
if nums.count(a) >= 2:
    print(a * m)
else:
    nums = set(nums)
    nums.remove(a)
    b = max(nums)
    quo = m // (k + 1)
    remain = m % (k + 1)
    print(a, k, b, quo, remain)
    print((a * k + b) * quo + (remain * a))
