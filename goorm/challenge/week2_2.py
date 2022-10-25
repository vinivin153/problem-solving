# 철자 분리 집합
import sys

input = sys.stdin.readline
n = int(input())
arr = input()
cnt = 1
for i in range(n - 1):
    if arr[i + 1] == arr[i]:
        continue
    else:
        cnt += 1

print(cnt)
