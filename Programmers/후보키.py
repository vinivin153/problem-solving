from itertools import combinations


def solution(relation):
    row, col = len(relation), len(relation[0])
    # 열끼리 묶기
    s = list(map(list, zip(*relation)))

    # 후보키 속성
    attribute = []
    # 속성의 조합 수(1부터 속성의 수까지)
    for i in range(1, col + 1):
        for c in combinations(range(col), i):
            # 조합한 속성들이 후보키와 겹치는 경우 찾기(최소성)
            for at in attribute:
                if at.issubset(set(c)):
                    break
            else:
                # 유일성 만족하는지 확인
                ckey = set()
                # 조합한 속성들의 열만 뽑기
                v = [s[idx] for idx in c]
                # 행끼리 묶어서 중복이 있는지 확인
                for j in zip(*v):
                    if j in ckey:
                        break
                    else:
                        ckey.add(j)
                else:
                    # 후보키를 만족하는 경우 추가
                    attribute.append(set(c))

    return len(attribute)
