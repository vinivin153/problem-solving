# 경로의 개수
import sys

input = sys.stdin.readline
n = int(input())
bridges = list(map(int, input().split()))

res = 1
for bridge in bridges:
    res *= bridge

print(res)
