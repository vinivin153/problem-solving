import sys

input = sys.stdin.readline

n, m = map(int, input().split())
time = list(map(int, input().split()))

if n <= m:
    print(n)
    sys.exit()

answer = 0
left = 1
right = n * 30
cnt = 0
while left <= right:
    mid = (left + right) // 2
    cnt = m
    for t in time:
        q, r = divmod(mid, t)
        cnt += q

    if cnt < n:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

temp = []
for idx, i in enumerate(time):
    # 나누어 떨어지는 경우
    if answer % i == 0:
        temp.append(idx)

temp.sort(reverse=True)
print(temp[cnt - n] + 1)
