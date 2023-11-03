def solution(dirs):
    s = set()
    x, y = 5, 5

    for dir in dirs:
        if dir == "U" and x > 0:
            if (x, y, x - 1, y) not in s and (x - 1, y, x, y) not in s:
                s.add((x, y, x - 1, y))
            x -= 1
        elif dir == "D" and x < 10:
            if (x, y, x + 1, y) not in s and (x + 1, y, x, y) not in s:
                s.add((x, y, x + 1, y))
            x += 1
        elif dir == "L" and y > 0:
            if (x, y, x, y - 1) not in s and (x, y - 1, x, y) not in s:
                s.add((x, y, x, y - 1))
            y -= 1
        elif dir == "R" and y < 10:
            if (x, y, x, y + 1) not in s and (x, y + 1, x, y) not in s:
                s.add((x, y, x, y + 1))
            y += 1

    return len(s)
