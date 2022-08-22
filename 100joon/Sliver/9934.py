import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
n = 2**k - 1
arr = list(map(int, input().split()))

queue = deque()

pre = 2**k // 4
queue.append((n // 2, pre))
while queue:
    i, j = queue.popleft()
    if pre != j:
        print()
    print(arr[i], end=" ")
    pre = j
    if j != 0:
        queue.append((i - j, j // 2))
        queue.append((i + j, j // 2))
