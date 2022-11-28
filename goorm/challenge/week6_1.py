# 7게임
import sys

input = sys.stdin.readline

for _ in range(5):
    k = list(map(int, input().rstrip()))
    a = k[0] + k[2] + k[4] + k[6]
    ans = a
    if k[1]:
        ans *= k[1]
    if k[3]:
        ans *= k[3]
    if k[5]:
        ans *= k[5]
    print(ans % 10)
