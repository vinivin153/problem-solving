import sys

input = sys.stdin.readline

n = int(input())
MAX_ALPHA = 26
MAX_NUMBER = 9

k = n
alpha = 0
number = 0
while k > 0:
    for _ in range(k):
        # 알파벳 출력
        print(chr(alpha + ord("A")), end=" ")
        alpha = (alpha + 1) % MAX_ALPHA

    for _ in range(n - k + 1):
        # 숫자 출력
        print(number + 1, end=" ")
        number = (number + 1) % MAX_NUMBER

    print()
    k -= 1
