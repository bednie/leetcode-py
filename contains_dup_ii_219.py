from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k >= len(nums) - 1:
            k = len(nums) - 1

        # frequency of elements in k window
        freqs = defaultdict(int)
        start, end = 0, k + 1

        # initialize
        for i in range(k + 1):
            freqs[nums[i]] += 1
            if freqs[nums[i]] == 2:
                return True

        # maintain freqs
        while end < len(nums):
            freqs[nums[start]] -= 1
            freqs[nums[end]] += 1

            if freqs[nums[end]] == 2:
                return True

            start += 1
            end += 1
