def solution(plans):
    plans.sort(key=lambda x: x[1], reverse=True)

    working = []
    result = []
    current_time = 0
    while plans:
        plan = plans.pop()
        name, start, left = plan
        left = int(left)
        hh, mm = map(int, start.split(":"))
        start_time = 60 * hh + mm

        # 작업중인 과제가 없는 경우
        if not working:
            # 작업추가
            working.append([name, left])
            # 현재시간 업데이트
            current_time = start_time
            continue

        # 현재 작업중인 과제가 끝나는 시간
        end_time = current_time + working[-1][1]
        # 현재 새로 들어온 과제가 작업중인 과제 끝나는 시간 보다 빠를 경우
        if end_time > start_time:
            # 작업중인 과제 남은 시간 업데이트
            working[-1][1] -= start_time - current_time
            # 현재 작업중인 과제 업데이트
            working.append([name, left])
            # 현재 시간 업데이트
            current_time = start_time
        else:
            # 작업중인 과제 마치기
            name, left = working.pop()
            # 현재 시간 업데이트
            current_time += left
            # 결과에 추가
            result.append(name)
            plans.append(plan)

    while working:
        name, left = working.pop()
        result.append(name)

    print(result)
