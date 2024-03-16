from typing import List

# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for
# one element which appears only once.

# Python dictionaries are hash tables, so I thought this might be faster than
# the "asnwer ^= num" method. However, many of the solutions take
# about 110ms on leetcode--including this one--so it's hard to tell.

# https://mail.python.org/pipermail/python-list/2000-March/048085.html


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1  # seen one time
            else:
                seen.pop(i)  # seen twice

        return seen.popitem()[0]


solution = Solution()
assert solution.singleNumber([4, 1, 2, 1, 2]), 4
