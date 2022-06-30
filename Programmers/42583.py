# 스택/큐 다리를 지나는 트럭

from collections import deque


def solution(bridge_length, weight, truck_weights):
    sum_weight = 0
    truck = deque(truck_weights)
    bridge = deque()

    time = 0
    while truck:
        x = truck[0]
        if sum_weight + x <= weight and len(bridge) < bridge_length:
            sum_weight += x
            bridge.appendleft(x)
            truck.popleft()
            time += 1
        else:
            k = bridge_length - len(bridge)
            time += k
            for _ in range(k):
                bridge.appendleft()
            sum_weight -= bridge.pop()

    time += bridge_length

    return time
