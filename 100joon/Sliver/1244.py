import sys

input = sys.stdin.readline

n = int(input())
switch = [0] + list(map(int, input().split()))
for _ in range(int(input())):
    gender, num = map(int, input().split())

    # 남자인 경우
    if gender == 1:
        for i in range(num, n + 1, num):
            switch[i] = abs(switch[i] - 1)
    # 여자인 경우
    else:
        j = 1
        switch[num] = abs(switch[num] - 1)
        while 0 < num - j and num + j <= n:
            left = num - j
            right = num + j
            if switch[left] == switch[right]:
                switch[left] = abs(switch[left] - 1)
                switch[right] = abs(switch[right] - 1)
                j += 1
            else:
                break

for i in range(1, n + 1):
    if i % 20 == 0:
        print(switch[i], end="\n")
    else:
        print(switch[i], end=" ")
