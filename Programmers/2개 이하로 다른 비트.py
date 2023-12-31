def solution(numbers):
    answer = []

    for number in numbers:
        # 짝수인 경우
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            # 홀수인 경우
            cnt = 0
            num = number
            while num:
                num //= 2
                left = num % 2
                if left == 0:
                    break
                cnt += 1
            answer.append(number + (2**cnt))

    return answer
