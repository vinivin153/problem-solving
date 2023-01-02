# 수식 최대화
from itertools import permutations


def solution(expression):
    nums = []
    operator = ["*", "+", "-"]

    num = ""
    for i in expression:
        if "0" <= i <= "9":
            num += i
        else:
            nums.append(num)
            num = ""
            nums.append(i)
    nums.append(num)

    answer = 0
    for i in permutations(operator):
        nums1 = nums[:]
        for j in i:
            new_nums = []
            k = 0
            while k < len(nums1):
                if j == nums1[k]:
                    num1 = new_nums.pop()
                    num2 = nums1[k + 1]
                    new_nums.append(str(eval(num1 + j + num2)))
                    k += 2
                else:
                    new_nums.append(nums1[k])
                    k += 1
            nums1 = new_nums[:]
        if abs(int(nums1[0])) > answer:
            answer = abs(int(nums1[0]))

    return answer
