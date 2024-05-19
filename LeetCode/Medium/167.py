from collections import Counter


class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)

        count = Counter(numbers)
        rnumbers = numbers[::-1]

        for i in range(n):
            diff = target - numbers[i]
            if diff in count:
                if diff == numbers[i] and count[diff] < 2:
                    continue

                idx = n - 1 - rnumbers.index(diff)
                if idx < i:
                    return [idx + 1, i + 1]
                else:
                    return [i + 1, idx + 1]


# two pointer
"""
class Solution(object):
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
"""
