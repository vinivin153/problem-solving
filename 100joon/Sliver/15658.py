import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
oper = list(map(int, input().split()))

max_v = -(10**10)
min_v = 10**10


def backtracking(value, cnt):
    global max_v, min_v
    if cnt == n - 1:
        max_v = max(max_v, value)
        min_v = min(min_v, value)
        return

    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            if i == 0:
                backtracking(value + nums[cnt + 1], cnt + 1)
            elif i == 1:
                backtracking(value - nums[cnt + 1], cnt + 1)
            elif i == 2:
                backtracking(value * nums[cnt + 1], cnt + 1)
            elif i == 3 and value < 0:
                backtracking(abs(value) // nums[cnt + 1] * -1, cnt + 1)
            else:
                backtracking(abs(value) // nums[cnt + 1], cnt + 1)
            oper[i] += 1


backtracking(nums[0], 0)
print(max_v)
print(min_v)
