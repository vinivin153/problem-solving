def solution(cap, n, deliveries, pickups):
    deli_stack = []
    pick_stack = []
    answer = 0

    for k, v in enumerate(deliveries):
        if v:
            deli_stack.append([k + 1, v])

    for k, v in enumerate(pickups):
        if v:
            pick_stack.append([k + 1, v])

    while deli_stack or pick_stack:
        if deli_stack and pick_stack:
            answer += max(deli_stack[-1][0], pick_stack[-1][0])
        elif pick_stack:
            answer += pick_stack[-1][0]
        else:
            answer += deli_stack[-1][0]

        left = cap
        while deli_stack:
            k, v = deli_stack.pop()
            if left > v:
                left -= v
                continue
            elif left < v:
                deli_stack.append([k, v - left])
                break
            else:
                break

        left = cap
        while pick_stack:
            k, v = pick_stack.pop()
            if left > v:
                left -= v
                continue
            elif left < v:
                pick_stack.append([k, v - left])
                break
            else:
                break

    return answer * 2
