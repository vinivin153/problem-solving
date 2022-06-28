# 완주하지 못한 선수


def solution(participant, completion):
    race = {}
    for name in participant:
        if name in race:
            race[name] += 1
        else:
            race[name] = 1

    for name in completion:
        race[name] -= 1

    for key, val in race.items():
        if val != 0:
            return key
