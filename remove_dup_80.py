from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        appended = 0
        while slow < len(nums) and fast < len(nums) and nums[fast] != "_":
            while nums[slow] == nums[fast] and fast - slow > 1:
                nums.pop(fast)
                nums.append("_")
                appended += 1 
            if nums[slow] != nums[fast]:
                slow = fast
            fast += 1 

        return len(nums) - appended