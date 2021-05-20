import sys

n = int(input())
withdraw_time = list(map(int, sys.stdin.readline().split()))
withdraw_time.sort()
spend_time = []
t = 0

for i in withdraw_time:
    t += i
    spend_time.append(t)


print(sum(spend_time))
