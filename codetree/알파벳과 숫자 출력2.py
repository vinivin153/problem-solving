n = int(input())

MAX_ALPHA = 26
MAX_NUMBER = 10


alpha = 0
number = 0
k = n
while k:
    for _ in range(k):
        print(chr(alpha + ord("A")), end=" ")
        alpha = (alpha + 1) % MAX_ALPHA

    for _ in range(n - k):
        print(number, end=" ")
        number = (number + 1) % MAX_NUMBER

    print()
    k -= 1


for _ in range(n):
    print(number, end=" ")
    number = (number + 1) % MAX_NUMBER
