import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lecture = list(map(int, input().split()))

answer = max(lecture)
left = answer
right = sum(lecture)
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    size = 0
    for i in lecture:
        if size + i > mid:
            size = i
            cnt += 1
        else:
            size += i

    if cnt <= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
