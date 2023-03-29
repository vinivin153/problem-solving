"""
ID, 문제번호, 점수
여러번 제출 가능, 최고 점수 -> 최종 점수

순위
1. 점수 같은 경우 풀이 제출 적은 팀 우선
2. 제출 횟수 동일시 마지막 제출 시간 빠른 팀 우선

점수 > 제출 수 > 마지막 제출 시간 
팀 순위 계산
"""

import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    # 팀의 수, 문제 수, 나의 팀, 로그 수
    n, k, my_id, m = map(int, input().split())
    team_score = [defaultdict(int) for _ in range(n + 1)]
    cnt_submit = [0] * (n + 1)
    recent_submit = [0] * (n + 1)
    for v in range(1, m + 1):
        # 팀 ID, 문제번호, 획득한 점수
        i, j, s = map(int, input().split())
        if team_score[i][j] < s:
            team_score[i][j] = s
        cnt_submit[i] += 1
        recent_submit[i] = v
    total_score = []
    for v in range(1, n + 1):
        total_score.append(
            [v, sum(team_score[v].values()), cnt_submit[v], recent_submit[v]]
        )

    total_score.sort(key=lambda x: [-x[1], x[2], x[3]])
    for v in range(n):
        if total_score[v][0] == my_id:
            print(v + 1)
            break
