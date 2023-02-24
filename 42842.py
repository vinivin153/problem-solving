# 카펫
def solution(brown, yellow):
    y = 3
    x = brown // 2 + 2 - y
    while x >= y:
        if yellow == (x - 2) * (y - 2):
            return [x, y]
        else:
            y += 1
            x = brown // 2 + 2 - y
