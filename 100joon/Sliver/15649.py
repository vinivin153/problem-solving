"""
solution 1
"""
from itertools import permutations

n, m = map(int, input().split())

nums = []
for i in range(n):
    nums.append(str(i + 1))

for i in permutations(nums, m):
    print(" ".join(i))


"""
solution2
"""
# n, m = map(int, input().split())

# nums = [0 for i in range(n)]


# def dfs(idx, cnt):
#     global stack
#     if cnt == m:
#         print(*stack)
#     else:
#         for i in range(n):
#             if nums[i]:
#                 continue
#             nums[i] = 1
#             stack.append(i + 1)
#             dfs(idx + 1, cnt + 1)
#             stack.pop()
#             nums[i] = 0


# stack = []
# dfs(0, 0)
