import heapq as hq


def solution(jobs):
    left_jobs = sorted(jobs, key=lambda x: (x[0], x[1]), reverse=True)

    current_time, waiting_time = 0, 0
    waiting_jobs = []
    hq.heappush(waiting_jobs, left_jobs.pop()[::-1])

    while waiting_jobs:
        work_time, at_time = hq.heappop(waiting_jobs)
        current_time = max(current_time, at_time) + work_time
        waiting_time += current_time - at_time

        while left_jobs and left_jobs[-1][0] <= current_time:
            hq.heappush(waiting_jobs, left_jobs.pop()[::-1])

        if left_jobs and not waiting_jobs:
            hq.heappush(waiting_jobs, left_jobs.pop()[::-1])

    return waiting_time // len(jobs)
