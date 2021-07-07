n = int(input())
way = input().split()

current = [1, 1]

for i in way:
    if i == "U" and current[0] > 1:
        current[0] += -1
    elif i == "D" and current[0] < n:
        current[0] += 1
    elif i == "L" and current[1] > 1:
        current[1] += -1
    elif i == "R" and current[1] < n:
        current[1] += 1

print(*current)
