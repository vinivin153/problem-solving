from itertools import permutations


def solution(numbers):
    numbers = sorted(list(numbers), reverse=True)
    MAX = int("".join(numbers)) + 2
    sieve = [False, False] + [True] * MAX

    for i in range(2, int(MAX**0.5) + 1):
        if sieve[i]:
            for j in range(i + i, MAX, i):
                sieve[j] = False

    answer = set()
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            k = int("".join(p))
            if sieve[k] and not k in answer:
                answer.add(k)

    return len(answer)
