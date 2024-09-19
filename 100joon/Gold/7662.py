from heapq import heappop, heappush

t = int(input())
for _ in range(t):
    k = int(input())
    removed = set()
    add_count = 0
    heap_max = []
    heap_min = []
    for _ in range(k):
        func, num = input().split()
        num = int(num)

        # 추가하는 기능
        if func == "I":
            add_count += 1
            heappush(heap_max, (num * -1, add_count))
            heappush(heap_min, (num, add_count))
        else:
            # 삭제하는 기능
            target = []
            if num == 1:
                target = heap_max
            else:
                target = heap_min

            # 비어있는 경우 넘어가기
            while target:
                # 제거된 인덱스가 아닌 경우
                if target[0][1] not in removed:
                    value, idx = heappop(target)
                    removed.add(idx)
                    break

                heappop(target)

    max_value, min_value = 0, 0
    if len(removed) == add_count:
        print("EMPTY")
    else:
        while heap_max:
            value, idx = heappop(heap_max)
            if idx not in removed:
                max_value = value * -1
                break

        while heap_min:
            value, idx = heappop(heap_min)
            if idx not in removed:
                min_value = value
                break
        print(max_value, min_value)
