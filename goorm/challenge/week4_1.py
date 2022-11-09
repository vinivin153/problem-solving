# 체크 카드
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

DEPOSIT = "deposit"
PAY = "pay"
RESERVATION = "reservation"
MONEY = n
waiting_list = deque()
for _ in range(m):
    order, amount = map(str, input().split())
    amount = int(amount)
    if order == DEPOSIT:
        MONEY += amount
        while waiting_list:
            if waiting_list[0] <= MONEY:
                MONEY -= waiting_list.popleft()
            else:
                break
    elif order == PAY:
        if MONEY >= amount:
            MONEY -= amount
    elif order == RESERVATION:
        if not waiting_list and MONEY >= amount:
            MONEY -= amount
        else:
            waiting_list.append(amount)

print(MONEY)
