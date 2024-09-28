from math import floor, sqrt, ceil


def solution(r1, r2):
    ans = 0

    rr1 = pow(r1, 2)
    rr2 = pow(r2, 2)

    for i in range(1, r2 + 1):
        ii = pow(i, 2)
        if i < r1:
            ans += floor(sqrt(rr2 - ii)) - ceil(sqrt(rr1 - ii)) + 1
        else:
            ans += floor(sqrt(rr2 - ii)) + 1

    return ans * 4
