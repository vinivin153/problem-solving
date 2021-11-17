import sys

input = sys.stdin.readline

work = []
n = int(input())
for i in range(n):
    d, w = map(int, input().split())
    work.append([d, w])

work.sort()
work.insert(0, 0)
max_score = 0
for i in range(work[-1][0], 0, -1):
    m = 0
    idx = 0
    for j in range(1, len(work)):
        if m < work[j][1] and work[j][0] >= i:
            idx = j
            m = work[j][1]

    if idx:
        max_score += work.pop(idx)[1]


print(max_score)
