def solution(k, dungeons):
    dungeons.sort()
    answer = []
    n = len(dungeons)
    visited = [0] * 8

    def backtracking(kk, cnt):
        for i in range(n):
            if visited[i] == 0:
                if kk >= dungeons[i][0]:
                    visited[i] = 1
                    backtracking(kk - dungeons[i][1], cnt + 1)
                    visited[i] = 0
                else:
                    answer.append(cnt)
                    return

        answer.append(cnt)

    backtracking(k, 0)
    return max(answer)
