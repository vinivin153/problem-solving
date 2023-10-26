def solution(command):
    loc = 0
    x, y = 0, 0

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for c in command:
        if c == "R":
            loc = (loc + 1) % 4
        elif c == "L":
            loc = (loc - 1) % 4
        elif c == "G":
            x += dx[loc]
            y += dy[loc]
        elif c == "B":
            x -= dx[loc]
            y -= dy[loc]

    return [x, y]
