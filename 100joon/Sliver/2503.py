import sys


input = sys.stdin.readline

nums = []
visited = [False] * 10


def make_number(val, cnt):
    if cnt == 3:
        nums.append(val)

    for i in range(1, 10):
        if not visited[i]:
            visited[i] = True
            make_number(val + str(i), cnt + 1)
            visited[i] = False


make_number("", 0)
ans = 0
n = int(input())


for _ in range(n):
    s, b = 0, 0
    num, strike, ball = map(str, input().split())
    strike, ball = int(strike), int(ball)
    tmp = []
    for i in nums:
        s, b = 0, 0
        if i[0] in num:
            if i[0] == num[0]:
                s += 1
            else:
                b += 1

        if i[1] in num:
            if i[1] == num[1]:
                s += 1
            else:
                b += 1

        if i[2] in num:
            if i[2] == num[2]:
                s += 1
            else:
                b += 1
        if s != strike or b != ball:
            tmp.append(i)
    for i in tmp:
        nums.remove(i)

print(len(nums))
