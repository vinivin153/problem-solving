answer = 0


def solution(ability):
    sports = len(ability[0])
    students = len(ability)
    print(sports, students)

    visited = [False] * students

    def backtracking(cnt, value):
        global answer

        if cnt == sports:
            if answer < value:
                answer = value
            return

        for i in range(students):
            if not visited[i]:
                visited[i] = True
                backtracking(cnt + 1, value + ability[i][cnt])
                visited[i] = False

    backtracking(0, 0)
    return answer
