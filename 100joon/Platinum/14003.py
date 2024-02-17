import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lis = [arr[0]]
dp = []


def bs(num):
    left = 0
    right = len(lis) - 1
    while left <= right:
        mid = (left + right) // 2

        if lis[mid] == num:
            return mid
        elif lis[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    return left


for num in arr:
    if num > lis[-1]:
        lis.append(num)
        dp.append([len(lis) - 1, num])
    else:
        idx = bs(num)
        lis[idx] = num
        dp.append([idx, num])

answer = []
idx_lis = len(lis) - 1
for idx, num in dp[::-1]:
    if idx == idx_lis:
        answer.append(num)
        idx_lis -= 1

print(len(answer))
print(*answer[::-1])
