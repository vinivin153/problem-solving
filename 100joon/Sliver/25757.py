import sys

input = sys.stdin.readline

n, g = map(str, input().rstrip().split())
players = set()
for _ in range(int(n)):
    players.add(input().rstrip())

players_nums = len(players)
if g == "Y":
    print(players_nums)
elif g == "F":
    print(players_nums // 2)
else:
    print(players_nums // 3)
