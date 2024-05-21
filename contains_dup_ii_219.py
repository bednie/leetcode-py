from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 1:
            return False

        if k >= len(nums) - 1:
            k = len(nums) - 1

        # frequency of elements in window length k
        freqs = {}
        start, end = 0, k + 1

        # initialize
        for i in range(k + 1):
            if nums[i] not in freqs:
                freqs[nums[i]] = 1
            else:
                return True

        # maintain freqs
        while end < len(nums):
            freqs[nums[start]] -= 1

            if nums[end] not in freqs:
                freqs[nums[end]] = 1

            elif freqs[nums[end]] >= 0:
                freqs[nums[end]] += 1

            if freqs[nums[end]] >= 2:
                return True

            start += 1
            end += 1
