from collections import defaultdict


def solution(info, query):
    score = defaultdict(list)

    for i in info:
        a, b, c, d, e = i.split()
        f = "-"
        for x in [a, f]:
            for y in [b, f]:
                for z in [c, f]:
                    for w in [d, f]:
                        score[(x, y, z, w)].append(int(e))

    for s in score.values():
        s.sort()

    answer = []
    for q in query:
        q = q.split()
        a, b, c, d = q[0], q[2], q[4], q[6]
        e = int(q[7])

        cnt = 0
        left, right = 0, len(score[(a, b, c, d)]) - 1
        while left <= right:
            mid = (left + right) // 2
            if score[(a, b, c, d)][mid] >= e:
                right = mid - 1
            else:
                left = mid + 1

        answer.append(len(score[(a, b, c, d)]) - left)

    return answer
