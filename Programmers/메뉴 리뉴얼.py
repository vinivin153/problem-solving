from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    menu = {}
    for i in course:
        menu[i] = defaultdict(int)

    course = set(course)
    for order in orders:
        order = sorted(order)
        for i in course:
            for comb in combinations(order, i):
                menu[i]["".join(comb)] += 1

    answer = []
    for k, v in menu.items():
        max_values = [m for m, n in v.items() if max(v.values()) == n and n != 1]
        answer += max_values

    return sorted(answer)
