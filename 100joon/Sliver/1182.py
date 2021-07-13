import sys

n, s = map(int, input().split())
nums = list(map(int, input().split()))

result = 0


def backTracking(idx, hap):
    global result
    if idx >= n:
        return
    hap += nums[idx]
    if hap == s:
        result += 1
    backTracking(idx + 1, hap)
    backTracking(idx + 1, hap - nums[idx])


backTracking(0, 0)
print(result)
