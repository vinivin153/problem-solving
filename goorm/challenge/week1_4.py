# 소수 찾기
import sys

input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
MAX_NUM = n + 1

primeNums = [True] * MAX_NUM
primeNums[1] = False


def eratos():
    m = int(MAX_NUM**0.5)
    for i in range(2, m + 1):
        if primeNums[i] == True:
            for j in range(i + i, MAX_NUM, i):
                primeNums[j] = False


eratos()
res = 0
for i in range(1, n + 1):
    if primeNums[i]:
        res += arr[i]
print(res)
