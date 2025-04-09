import sys

input = sys.stdin.readline
n, m = map(int, input().split())
rest_days = set()
if m > 0:
    rest_days = set(map(int, input().split()))

# dp[day][coupon] = day일차에 coupon개의 쿠폰을 가지고 있을 때의 최소 비용
dp = [[-1] * 41 for _ in range(n + 1)]


def solve(day, coupon):
    # 모든 날짜를 다 처리한 경우
    if day > n:
        return 0

    # 이미 계산된 값이 있으면 반환
    if dp[day][coupon] != -1:
        return dp[day][coupon]

    # 쉬는 날인 경우 다음 날로 넘어감
    if day in rest_days:
        dp[day][coupon] = solve(day + 1, coupon)
        return dp[day][coupon]

    # 1일권 구매
    cost = solve(day + 1, coupon) + 10000

    # 3일권 구매 (쿠폰 1장 획득)
    cost = min(cost, solve(day + 3, coupon + 1) + 25000)

    # 5일권 구매 (쿠폰 2장 획득)
    cost = min(cost, solve(day + 5, coupon + 2) + 37000)

    # 쿠폰 3장 사용
    if coupon >= 3:
        cost = min(cost, solve(day + 1, coupon - 3))

    dp[day][coupon] = cost
    return cost


print(solve(1, 0))
