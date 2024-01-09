from collections import defaultdict
from itertools import combinations


def solution(friends, gifts):
    gscore = defaultdict(int)
    glog = {friend: defaultdict(int) for friend in friends}

    for gift in gifts:
        give, take = gift.split()
        gscore[give] += 1
        gscore[take] -= 1
        glog[give][take] += 1

    answer = defaultdict(int)
    for i, j in combinations(friends, 2):
        if glog[i][j] > glog[j][i]:
            answer[i] += 1
        elif glog[i][j] < glog[j][i]:
            answer[j] += 1
        else:
            if gscore[i] > gscore[j]:
                answer[i] += 1
            elif gscore[i] < gscore[j]:
                answer[j] += 1

    if answer:
        return max(answer.values())
    else:
        return 0
