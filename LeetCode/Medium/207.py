# 207. Course Schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(x):
            if x in cycle:
                return True

            if visited[x] == 1:
                return False

            visited[x] = 1
            cycle.add(x)

            for i in graph[x]:
                if dfs(i):
                    return True

            cycle.remove(x)
            return False

        graph = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[a].append(b)

        visited = [0] * numCourses
        cycle = set()

        for i in range(numCourses):
            if dfs(i):
                return False

        return True
