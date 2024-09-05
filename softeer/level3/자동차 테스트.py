import sys
from bisect import bisect_left

input = sys.stdin.readline

n, m = map(int, input().split())
cars = sorted(list(map(int, input().split())))
set_cars = set(cars)
for _ in range(m):
    k = int(input())
    if k not in set_cars:
        print(0)
        continue

    idx = 0
    left, right = 0, n - 1
    while left <= right:
        mid = (left + right) // 2

        if cars[mid] == k:
            idx = mid
            break
        elif cars[mid] < k:
            left = mid + 1
        else:
            right = mid - 1

    if idx == 0 or idx == n - 1:
        print(0)
    else:
        print(idx * (n - idx - 1))


"""
bitsect 사용한 풀이

import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n, m = map(int, input().split())
cars = sorted(list(map(int, input().split())))
set_cars = set(cars)
for _ in range(m):
    k = int(input())
    if k not in set_cars:
        print(0)
        continue
    
    idx = bisect_left(cars, k)
    if idx == 0 or idx == n:
        print(0)
    else:
        print(idx * (n - idx - 1))
"""
