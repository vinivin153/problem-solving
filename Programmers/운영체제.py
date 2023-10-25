import heapq


def solution(program):
    program.sort(key=lambda x: (-x[1], -x[0]))
    waiting_time = [0] * 11
    waiting_list = []

    score, calltime, runtime = program.pop()
    time = calltime + runtime
    while program or waiting_list:
        if waiting_list:
            score, calltime, runtime = heapq.heappop(waiting_list)
            waiting_time[score] += time - calltime
            time += runtime

        while program and program[-1][1] <= time:
            heapq.heappush(waiting_list, program.pop())

        if not waiting_list and program:
            _, calltime, runtime = program.pop()
            time = calltime + runtime

    return [time] + waiting_time[1:]
