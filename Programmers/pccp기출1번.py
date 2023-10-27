def solution(bandage, health, attacks):
    atk = 0
    t, heal, plusheal = bandage
    hp = health
    cnt = 0
    for i in range(1, 1001):
        # 공격 시간인 경우
        if attacks[atk][0] == i:
            # 체력 감소
            hp -= attacks[atk][1]
            cnt = 0
            # 몬스터의 공격을 받고 캐릭터의 체력이 0 이하가 되어 죽는다면 -1을 return
            if hp <= 0:
                return -1

            if len(attacks) - 1 == atk:
                break
            else:
                atk += 1
        else:
            # 회복
            cnt += 1
            # 최대 체력인 경우 넘어감
            if hp == health:
                continue
            else:
                hp += heal
                if cnt == t:
                    hp += plusheal
                    cnt = 0
                hp = min(hp, health)
    return hp
