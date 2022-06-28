# 전화번호 목록


def solution(phone_book):
    nums = {}

    for number in phone_book:
        nums[number] = 1

    for number in phone_book:
        head = ""
        for n in number:
            head += n
            if head in nums:
                if head != number:
                    return False
        nums[head] = 1

    return True


print(solution(["119", "97674223", "1195524421"]))
