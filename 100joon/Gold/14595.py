import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
destroy = sorted([list(map(int, input().split())) for _ in range(m)])

room_cnt = n
prev = 0
end = 0
for a, b in destroy:
    if end > b:
        continue

    if prev <= a <= end:
        if b > end:
            end = b
    else:
        room_cnt -= end - prev
        prev = a
        end = b

room_cnt -= end - prev

print(room_cnt)
