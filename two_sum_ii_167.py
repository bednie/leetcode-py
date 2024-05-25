from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        memo = {}
        for i, j in enumerate(numbers):
            if (target - j) in memo and memo[target - j] != i:
                return [memo[target - j] + 1, i + 1]
            memo[j] = i
