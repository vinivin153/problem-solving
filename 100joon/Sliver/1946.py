"""
my solution
"""
import sys


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline())
    score = []
    cnt = 1
    for _ in range(n):
        score.append(list(map(int, sys.stdin.readline().split())))
    score.sort()
    min_num = score[0][1]
    for i in range(1, n):
        if score[i][1] < min_num:
            cnt += 1
            min_num = score[i][1]

    print(cnt)


"""
best solution(not using sort)
"""
# import sys


# t = int(input())
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     score = [0] * (n + 1)
#     cnt = 1
#     for _ in range(n):
#         a, b = map(int, sys.stdin.readline().split())
#         score[a] = b
#     min_num = score[1]
#     for i in range(2, n + 1):
#         if score[i] < min_num:
#             cnt += 1
#             min_num = score[i]

#     print(cnt)
