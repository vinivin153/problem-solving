import sys
import math

input = sys.stdin.readline
n, atk = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]

answer = 0
left = 1
right = 999999000001 * n
while left <= right:
    mid = (left + right) // 2
    cur_atk = atk
    isDead = False
    hp = mid
    for t, a, h in info:
        if t == 1:
            cnt_userAtk = math.ceil(h / cur_atk)
            cnt_mAtk = math.ceil(hp / a)
            if cnt_userAtk <= cnt_mAtk:
                hp -= (cnt_userAtk - 1) * a
            else:
                isDead = True
                break
        else:
            cur_atk += a
            hp = min(mid, hp + h)

    if isDead:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)
