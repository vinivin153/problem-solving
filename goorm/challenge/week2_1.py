# 합격자 찾기
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    avg = sum(arr) / n
    cnt = 0
    for s in arr:
        if s >= avg:
            cnt += 1
    print(f"{cnt}/{n}")
