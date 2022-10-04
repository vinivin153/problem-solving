# Best Sightseeing Pair
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        dist = 1
        max_value = 0
        for j in range(1, len(values)):
            score = values[i] + values[j] - dist
            max_value = max(max_value, score)

            if values[i] - dist < values[j]:
                i = j
                dist = 1
            else:
                dist += 1
        return max_value
