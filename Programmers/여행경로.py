from collections import defaultdict

answer = 0
end = False


def solution(tickets):
    visited = defaultdict(int)
    flight = defaultdict(list)
    for ticket in tickets:
        a, b = ticket
        flight[a].append(b)
        visited[a + b] += 1
    for k, v in flight.items():
        v.sort()

    t = len(tickets)

    def backtracking(result):
        global end, answer

        if t + 1 == len(result):
            end = True
            answer = result
            return

        for f in flight[result[-1]]:
            c = result[-1] + f
            if visited[c] > 0:
                visited[c] -= 1
                backtracking(result + [f])
                visited[c] += 1
            if end:
                return

    backtracking(["ICN"])
    return answer
