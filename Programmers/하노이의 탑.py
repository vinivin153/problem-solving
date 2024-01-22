answer = []


def move(start, to):
    answer.append([start, to])


def hanoi(n, start, to, via):
    if n == 1:
        move(start, to)
        return

    hanoi(n - 1, start, via, to)
    move(start, to)
    hanoi(n - 1, via, to, start)


def solution(n):
    hanoi(n, 1, 3, 2)

    return answer
