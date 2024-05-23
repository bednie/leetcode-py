from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        start = 0
        end = 0
        summary = []

        while end < len(nums):
            while end < len(nums) - 1 and nums[end + 1] == nums[end] + 1:
                end += 1

            if start == end:
                summary.append(f"{nums[end]}")
            else:
                summary.append(f"{nums[start]}->{nums[end]}")
            end += 1
            start = end

        return summary
