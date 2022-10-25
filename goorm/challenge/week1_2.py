# 동명이인
import sys

input = sys.stdin.readline
n, name = input().split()

res = 0
for _ in range(int(n)):
    student = input().rstrip()
    if name in student:
        res += 1
print(res)
