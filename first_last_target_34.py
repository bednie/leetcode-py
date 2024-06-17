from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = [-1, -1]
        left, right = 0, len(nums) - 1
        in_range = - 1

        # edge cases
        if not nums:
            return output

        if nums[left] == target and nums[right] == target:
            return [left, right]

        if nums[left] == target and nums[left+1] != target:
            return [left, left]

        if nums[right] == target and nums[right-1] != target:
            return [right, right]
        
        # find range
        while left <= right:
            mid = right + left // 2

            if nums[mid] > target:
                right = mid - 1

            elif nums[mid] < target:
                left = mid + 1

            else:
                in_range = mid
                break

        # left
        left, right = 0, in_range
        while left <= right:
            mid = right + left // 2

            if nums[right] == target and nums[right-1] != target:
                output[0] = right
                break

            if nums[mid] == target:
                right = mid - 1

            else:
                left = mid + 1

        # right
        left, right = in_range, len(nums) - 1
        while left <= right:
            mid = right + left // 2

            if nums[right] == target:
                output[1] = right
                break

            if nums[left] == target and nums[left+1] != target:
                output[1] = left
                break

            if nums[mid] == target:
                left = mid + 1

            else:
                right = mid - 1

        return output
