import sys

input = sys.stdin.readline

n = int(input())

meeting = [list(map(int, input().split())) for _ in range(n)]
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 0
end_time = meeting[0][0]
for i in range(n):
    if meeting[i][0] >= end_time:
        cnt += 1
        end_time = meeting[i][1]

print(cnt)
