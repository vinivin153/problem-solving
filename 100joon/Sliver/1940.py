import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
nums = list(map(int, input().split()))
nums.sort()


res = 0

# sol1 backtracking
"""
visited = set()
def backtracking(val, k, cnt):
    global res
    if cnt == 2:
        if val == m:
            res += 1
        return

    for i in range(k, n):
        if val + nums[i] > m:
            return
        if nums[i] not in visited:
            visited.add(nums[i])
            backtracking(val + nums[i], i + 1, cnt + 1)
            visited.remove(nums[i])

backtracking(0, 0, 0)
"""

# sol2 two pointer
left = 0
right = n - 1
while left < right:
    k = nums[left] + nums[right]
    if m == k:
        right -= 1
        left += 1
        res += 1
    elif k < m:
        left += 1
    else:
        right -= 1

print(res)
