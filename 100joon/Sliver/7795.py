import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = sorted(map(int, input().split()), reverse=True)
    b = sorted(map(int, input().split()))

    answer = 0

    for aa in a:
        left = 0
        right = m - 1
        cnt = 0
        while left <= right:
            mid = (left + right) // 2

            if b[mid] < aa:
                cnt = mid + 1
                left = mid + 1
            else:
                right = mid - 1
        answer += cnt

    print(answer)
