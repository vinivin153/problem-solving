# 1079. Letter Tile Possibilities


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtracking(v, s):
            t = "".join(s)
            if t in k:
                return
            else:
                k.add(t)

            for i in range(len(tiles)):
                if visited[i] == 0:
                    visited[i] = 1
                    s.append(tiles[i])
                    backtracking(i, s)
                    s.pop()
                    visited[i] = 0

        visited = [0] * 7
        k = set()

        backtracking(0, [])

        return len(k) - 1
