import sys

sys.setrecursionlimit(100000)


def init(start, end, idx):
    if start == end:
        segmentTree[idx] = nums[start]
        return segmentTree[idx]

    mid = (start + end) // 2
    segmentTree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return segmentTree[idx]


def prefix_sum(start, end, idx, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return segmentTree[idx]
    mid = (start + end) // 2
    return prefix_sum(start, mid, idx * 2, left, right) + prefix_sum(
        mid + 1, end, idx * 2 + 1, left, right
    )


def update(start, end, idx, diff, diff_idx):
    if diff_idx > end or diff_idx < start:
        return
    segmentTree[idx] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, idx * 2, diff, diff_idx)
    update(mid + 1, end, idx * 2 + 1, diff, diff_idx)


n, m, k = map(int, input().split())

nums = []
for i in range(n):
    nums.append(int(input()))

# v = 1
# while True:
#     if n <= v * v:
#         v = v * v * 2
#         break
#     v += 1

segmentTree = [0] * n * 4

init(0, n - 1, 1)
for i in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(1, n, 1, c - nums[b - 1], b)
        nums[b - 1] = c
    else:
        print(prefix_sum(1, n, 1, b, c))
