def solution(bandage, health, attacks):
    t, x, y = bandage
    hp = health
    lastAttack = attacks[-1][0]

    atkIdx = 0
    cnt = 0
    for time in range(1, lastAttack + 1):
        # 공격 당하는 경우
        if attacks[atkIdx][0] == time:
            hp -= attacks[atkIdx][1]
            cnt = 0
            atkIdx += 1
            if hp <= 0:
                return -1
        # 체력 회복하는 경우
        else:
            cnt += 1
            hp = min(hp + x, health)
            if cnt == t:
                hp = min(hp + y, health)
                cnt = 0

    return hp
