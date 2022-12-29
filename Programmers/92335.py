# k진수에서 소수 개수 구하기
def solution(n, k):
    def trans(num):
        if num == 0:
            return ""

        return trans(num // k) + str(num % k)

    def isPrime(k):
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                return False

        return True

    answer = 0
    nums = trans(n).split("0")

    for i in nums:
        if i == "1" or i == "":
            continue
        if isPrime(int(i)):
            answer += 1

    return answer
