import sys

input = sys.stdin.readline
start = list(map(int, input().split()))
end = list(map(int, input().split()))
teleport = []
for _ in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    teleport.append([[x1, y1], [x2, y2]])


def cal_dist(a, b):
    r1, c1 = a
    r2, c2 = b
    return abs(r1 - r2) + abs(c1 - c2)


def cal(route):
    if not route:
        return cal_dist(start, end)

    dist = 10
    # 시작지점에서 텔레포트 하는 지점까지 거리
    dist += cal_dist(start, route[0][0])
    # 마지막 텔레포트 지점에서 도착지점까지 거리
    dist += cal_dist(route[-1][1], end)

    # 텔레포트하는 사이의 거리
    for i in range(1, len(route)):
        dist += cal_dist(route[i - 1][1], route[i][0]) + 10
    return dist


visited = [False] * 3
ans = []


def dfs(cnt, route):
    ans.append(cal(route))

    if cnt == 3:
        return

    for i in range(3):
        if not visited[i]:
            visited[i] = True
            dfs(cnt + 1, route + [teleport[i]])
            dfs(cnt + 1, route + [teleport[i][::-1]])
            visited[i] = False


dfs(0, [])
print(min(ans))
