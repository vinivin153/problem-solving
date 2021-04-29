import sys

t = int(input())

for _ in range(t):
    l, n = map(int, sys.stdin.readline().split())

    ant = []

    for _ in range(n):
        ant.append(int(sys.stdin.readline()))  # 개미의 위치 설정

    ant.append(l / 2)  # 가운데 설정
    ant.sort()  # 정렬
    mid_index = ant.index(l / 2)
    if mid_index != 0 and mid_index != len(ant) - 1:  # 가운데 인덱스 양옆 모두 존재할 때
        print(max(ant[mid_index - 1], l - ant[mid_index + 1]), max(l - ant[0], ant[-1]))
    elif mid_index == 0:
        print(l - ant[mid_index + 1], max(l - ant[0], ant[-1]))
    else:
        print(ant[mid_index - 1], max(l - ant[0], ant[-1]))

