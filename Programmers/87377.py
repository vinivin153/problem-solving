from itertools import combinations

point_x = []
point_y = []
ans = []


def drawStars():
    diff_x = min(point_x) * -1
    diff_y = max(point_y) * -1
    for i in range(len(point_x)):
        point_x[i] = abs(point_x[i] + diff_x)
        point_y[i] = abs(point_y[i] + diff_y)

    mat = [["." for _ in range(max(point_x) + 1)] for _ in range(max(point_y) + 1)]

    for i in range(len(point_x)):
        mat[point_y[i]][point_x[i]] = "*"

    for i in mat:
        ans.append("".join(i))


def findIntersectionPoint(line1, line2):
    a, b, e = line1
    c, d, f = line2
    if (a * d - b * c) != 0:
        x = (b * f - e * d) / (a * d - b * c)
        y = (e * c - a * f) / (a * d - b * c)
        if x % 1 == 0 and y % 1 == 0:
            point_x.append(int(x))
            point_y.append(int(y))


def solution(line):
    for a, b in combinations(range(0, len(line)), 2):
        findIntersectionPoint(line[a], line[b])
    drawStars()
    return ans
