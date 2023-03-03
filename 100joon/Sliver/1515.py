n = input()

current = 1
loc = 0


while loc < len(n):
    cur = str(current)
    for i in range(len(cur)):
        if n[loc] == cur[i]:
            loc += 1
            if loc >= len(n):
                break

    current += 1

print(current - 1)
