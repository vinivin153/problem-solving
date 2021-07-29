def cal_time(h, m):
    diff = eval(worker_utc[3:]) - eval(utc[3:])

    h += diff // 1
    m += diff % 1 * 60

    if m >= 60:
        h += 1
        m -= 60
    elif m < 0:
        h -= 1
        m += 60

    if h >= 24:
        h -= 24
    elif h < 0:
        h += 24

    print(f"{int(h):02}:{int(m):02}")


n = int(input())

time, utc = map(str, input().split())

hh = int(time[:2])
mm = int(time[3:])

for i in range(n):
    worker_utc = input()
    cal_time(hh, mm)
