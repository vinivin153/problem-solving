import sys


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    team_num = list(map(int, input().split()))

    teams = {}
    for num in team_num:
        if num in teams:
            teams[num] += 1
        else:
            teams[num] = 1

    for team, num in list(teams.items()):
        if num != 6:
            del teams[team]
        else:
            teams[team] = []

    score = 1
    for i in range(n):
        if team_num[i] in teams:
            teams[team_num[i]].append(score)
            score += 1

    rank = {}
    for team, scores in teams.items():
        rank[team] = sum(scores[:4])

    winner_score = 10000
    winner = 0

    for team, team_score in sorted(rank.items(), key=lambda x: x[1]):
        if team_score < winner_score:
            winner_score = team_score
            winner = team
        elif team_score == winner_score:
            if teams[team][4] < teams[winner][4]:
                winner = team
        else:
            break

    print(winner)
