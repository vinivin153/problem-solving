import sys

input = sys.stdin.readline
n = int(input())
pre_time = [0, 0]
score = [0, 0]
t1 = [0, 0]
t2 = [0, 0]


def time_cal(mm, ss):
    if score[0] > score[1]:
        if ss - pre_time[1] < 0:
            t1[0] += mm - pre_time[0] - 1
            t1[1] += ss + 60 - pre_time[1]
        else:
            t1[0] += mm - pre_time[0]
            t1[1] += ss - pre_time[1]
    elif score[0] < score[1]:
        if ss - pre_time[1] < 0:
            t2[0] += mm - pre_time[0] - 1
            t2[1] += ss + 60 - pre_time[1]
        else:
            t2[0] += mm - pre_time[0]
            t2[1] += ss - pre_time[1]


for _ in range(n):
    team, time = map(str, input().split())
    mm, ss = map(int, time.split(":"))

    time_cal(mm, ss)

    if team == "1":
        score[0] += 1
    else:
        score[1] += 1

    pre_time = [mm, ss]

time_cal(48, 0)

if t1[1] > 60:
    t1[0] += t1[1] // 60
    t1[1] = t1[1] % 60

if t2[1] > 60:
    t2[0] += t2[1] // 60
    t2[1] = t2[1] % 60

print(f"{t1[0]:02}:{t1[1]:02}")
print(f"{t2[0]:02}:{t2[1]:02}")
