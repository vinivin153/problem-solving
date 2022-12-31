# 거리두기 확인하기
from collections import deque


def solution(places):
    room = []

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    dx1 = [0, 0, 2, -2]
    dy1 = [2, -2, 0, 0]

    dx2 = [1, 1, -1, -1]
    dy2 = [-1, 1, -1, 1]

    def check():
        for x in range(5):
            for y in range(5):
                if room[x][y] == "P":
                    for i in range(4):
                        nx = dx[i] + x
                        ny = dy[i] + y
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if room[nx][ny] == "P":
                                return False

                    for i in range(4):
                        nx = dx1[i] + x
                        ny = dy1[i] + y
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if room[nx][ny] == "P":
                                if room[(nx + x) // 2][(ny + y) // 2] != "X":
                                    return False

                    for i in range(4):
                        nx = dx2[i] + x
                        ny = dy2[i] + y
                        if 0 <= nx < 5 and 0 <= ny < 5:
                            if room[nx][ny] == "P":
                                if (
                                    room[x + dx2[i]][y] != "X"
                                    or room[x][y + dy2[i]] != "X"
                                ):
                                    return False
        return True

    answer = []
    for place in places:
        room = []

        for p in place:
            room.append(list(p))

        if check():
            answer.append(1)
        else:
            answer.append(0)

    return answer
