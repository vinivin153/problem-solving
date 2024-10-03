from itertools import permutations


fatigue = {
    (0, "diamond"): 1,
    (0, "iron"): 1,
    (0, "stone"): 1,
    (1, "diamond"): 5,
    (1, "iron"): 1,
    (1, "stone"): 1,
    (2, "diamond"): 25,
    (2, "iron"): 5,
    (2, "stone"): 1,
}


def solution(picks, minerals):
    pick = []
    for i in range(3):
        for _ in range(picks[i]):
            if len(pick) < 10:
                pick.append(i)

    ans = 10**9
    for p in set(permutations(pick)):
        idx = 0
        count = 0
        sum1 = 0
        for m in minerals:
            sum1 += fatigue[(p[idx], m)]
            count += 1
            if count >= 5:
                count = 0
                idx += 1

            if idx >= len(p):
                break

        ans = min(sum1, ans)

    return ans
