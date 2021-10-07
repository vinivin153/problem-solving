# 841. Keys and Rooms
from collections import deque


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        cnt = len(rooms)
        visited = [0] * cnt
        visited[0] = 1
        cnt -= 1

        queue = deque()
        queue.append(0)
        while queue:
            current = queue.popleft()
            for i in rooms[current]:
                if visited[i] == 0:
                    visited[i] = 1
                    cnt -= 1
                    queue.append(i)

        return False if cnt else True
