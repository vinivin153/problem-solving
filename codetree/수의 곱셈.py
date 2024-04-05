"""
홀수가 짝수보다 우선순위가 높다.
같은 홀수끼리는 수 자체가 더 큰 경우가 우선순위가 높다.
같은 짝수끼리도 수 자체가 더 큰 경우가 우선순위가 높다.

1. 수가 가장 큰 홀수
2. 홀수가 없는 경우 가장 큰 짝수

홀수 * 홀수 = 홀수
홀수 * 짝수 = 짝수
짝수 * 짝수 = 짝수
"""

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
nums = [a, b, c]

nums.append(a * b)
nums.append(a * c)
nums.append(b * c)
nums.append(a * b * c)
nums.sort(key=lambda x: (x % 2 == 0, -x))

print(nums[0])
