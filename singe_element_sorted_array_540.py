from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # trivial case
        if len(nums) == 1:
            return nums[0]

        # iterative solution
        start = 0
        end = len(nums)
        midpoint = 0
        while len(nums[start:end]) > 3:
            midpoint = end - (end - start) // 2

            # make sure duplicate elements are in the same slice
            # check boundary and adjust midpoint if necessary
            if nums[midpoint - 1] == nums[midpoint]:
                midpoint -= 1

            # determine which slice's length is odd, then
            # update start and end for the next iteration
            if len(nums[start:midpoint]) % 2 == 1:
                end = midpoint
            else:
                start = midpoint

        if nums[start] == nums[start + 1]:
            return nums[end - 1]
        else:
            return nums[start]


solution = Solution()
solution = solution.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8])
print("Answer: " + str(solution))
assert solution == 2, "Wrong answer!"

solution2 = Solution()
solution2 = solution2.singleNonDuplicate([1, 1, 2, 2, 3])
print("Answer: " + str(solution2))
assert solution2 == 3, "Wrong answer!"

solution3 = Solution()
solution3 = solution3.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11])
print("Answer: " + str(solution3))
assert solution3 == 10, "Wrong answer!"
