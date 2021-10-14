# 547. Number of Provinces
from collections import deque


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def bfs(x):
            queue = deque()
            queue.append(x)
            visited[x] = 1
            while queue:
                current = queue.popleft()
                for i in range(len(isConnected[x])):
                    if visited[i] == 0 and isConnected[current][i] == 1:
                        queue.append(i)
                        visited[i] = 1

        visited = [0] * 201
        cnt = 0
        for i in range(len(isConnected)):
            if visited[i] == 0:
                bfs(i)
                cnt += 1

        return cnt
