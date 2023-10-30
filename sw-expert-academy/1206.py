T = 10
for test_case in range(1, T + 1):
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = 0

    for i in range(2, n - 2):
        left_max = max(buildings[i - 2], buildings[i - 1])
        right_max = max(buildings[i + 1], buildings[i + 2])

        if left_max < buildings[i] and right_max < buildings[i]:
            answer += buildings[i] - max(left_max, right_max)

    print(f"#{test_case} {answer}")
