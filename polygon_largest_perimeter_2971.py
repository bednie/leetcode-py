from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        def test_polygon(nums: List[int]) -> int:
            # no possible polygon
            if len(nums) < 3:
                return -1

            # test polygon
            if sum(nums[:-1]) > nums[-1]:
                return sum(nums)
            else:
                nums = nums[:-1]
                return test_polygon(nums)

        # sort input
        nums = sorted(nums)
        # initial call
        return test_polygon(nums)


solution = Solution()
print(solution.largestPerimeter([1, 12, 1, 2, 5, 50, 3]))
print(solution.largestPerimeter([5, 5, 50]))
print(solution.largestPerimeter([5, 5]))
