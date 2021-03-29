import sys
from collections import deque

n, m, start = map(int, sys.stdin.readline().split())

edge = {}
visited = []
stack = []
queue = deque()

# 딕셔너리에 key 와 value 추가 (간선의 정보)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if a in edge:
        edge[a].append(b)
    else:
        edge[a] = [b]

    if b in edge:
        edge[b].append(a)
    else:
        edge[b] = [a]

# value 값을 정렬
for k, v in edge.items():
    edge[k] = sorted(v)

stack.append(start)
cnt = 0
while len(stack) != 0:
    if cnt == n:  # 정점의 수 만큼 돌았다면 종료
        break
    current = stack.pop()
    if current in visited:
        continue
    cnt += 1
    print(current, end=" ")
    visited.append(current)
    try:  # 연결된 값 들을 가져온다
        for i in reversed(edge.get(current)):  # 낮은 번호 순으로 출력해야 해서 큰 수부터 넣는다
            if not i in visited:  # 방문하지 않았을 경우만 추가
                stack.append(i)
    except:
        continue
print()

visited.clear()  # 방문한 곳 초기화
queue.append(start)
cnt = 0
while len(queue) != 0:
    if cnt == n:
        break
    current = queue.popleft()
    cnt += 1
    print(current, end=" ")
    visited.append(current)
    try:
        for i in edge.get(current):
            if not i in visited and not i in queue:  # 방문하지 얺거나 queue에 없을경우에만 추가
                queue.append(i)
    except:
        continue
