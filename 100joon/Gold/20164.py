from itertools import combinations

n = input()


def count_odd(s):
    cnt = 0
    for i in s:
        if int(i) % 2 == 1:
            cnt += 1

    return cnt


def calc(snum):
    if len(snum) == 1:
        return count_odd(snum)
    elif len(snum) == 2:
        new_num = str(int(snum[0]) + int(snum[1]))
        return calc(new_num) + count_odd(snum)
    else:
        values = []
        for a, b in combinations(range(1, len(snum)), 2):
            new_num = str(int(snum[:a]) + int(snum[a:b]) + int(snum[b:]))
            values.append(calc(new_num))

        return max(values) + count_odd(snum)


def calc_min(snum):
    if len(snum) == 1:
        return count_odd(snum)
    elif len(snum) == 2:
        new_num = str(int(snum[0]) + int(snum[1]))
        return calc_min(new_num) + count_odd(snum)
    else:
        values = []
        for a, b in combinations(range(1, len(snum)), 2):
            new_num = str(int(snum[:a]) + int(snum[a:b]) + int(snum[b:]))
            values.append(calc_min(new_num))

        return min(values) + count_odd(snum)


print(calc_min(n), calc(n))
