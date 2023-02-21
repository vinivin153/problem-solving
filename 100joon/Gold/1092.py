"""
1. 컨테이너와 박스를 오름차순으로 정렬
2. 가장 큰 컨테이너와 가장 큰 박스를 비교해 옮길 수 있는지 확인
3. 최소시간 구하기
    a. 큰 수 부터 옮기기
"""

import sys

input = sys.stdin.readline
n = int(input())
c = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
b = sorted(list(map(int, input().split())), reverse=True)

if b[0] > c[0]:
    print(-1)
    sys.exit()

ans = 0

while b:
    ans += 1
    for i in c:
        flag = False
        for j in b:
            if i >= j:
                b.remove(j)
                flag = True
                break
        if not flag:
            break
print(ans)
