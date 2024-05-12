from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        copy_to = 1
        for next in range(1, len(nums)):
            if nums[next] != nums[next - 1]:
                nums[copy_to] = nums[next]
                copy_to += 1
        return copy_to


# test
sol = Solution()
print(sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
