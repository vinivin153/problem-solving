"""
g개의 그림문자, 문자열 S
단어 W가 마야 문자열 S에 들어있을 수 있는 모든 가짓수 계산
즉, 문자열  S안에서 문자열 W의 순열 중 하나가 부분 문자열로 들어있는 모든 경우의 수를 계산
"""
import sys
from collections import defaultdict, deque

input = sys.stdin.readline

g, s = map(int, input().split())
W = input().rstrip()
S = input().rstrip()

wd = defaultdict(int)
for i in W:
    wd[i] += 1

sd = defaultdict(int)
for i in S[:g]:
    sd[i] += 1

ans = 0
if sd == wd:
    ans += 1

for i in range(g, s):
    pre = i - g
    next = i
    if sd[S[pre]] == 1:
        sd.pop(S[pre])
    else:
        sd[S[pre]] -= 1

    sd[S[next]] += 1
    if sd == wd:
        ans += 1

print(ans)
