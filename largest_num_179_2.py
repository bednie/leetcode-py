from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 0:
            return ""
        elif len(nums) == 1:
            return str(nums[0])

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if int(str(nums[i]) + str(nums[j])) < int(str(nums[j]) + str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]

        max = "".join(str(num) for num in nums)
        if int(max) == 0:
            return "0"
        else:
            return max


solution = Solution()
assert (
    solution.largestNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) == "9876543210"
), "Wrong answer!"
print(solution.largestNumber([3, 30, 34, 5, 9]))
print(solution.largestNumber([0, 0, 1]))
print(solution.largestNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
print(solution.largestNumber([999999991, 9]))
print(
    solution.largestNumber(
        [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
    )
)
print(
    solution.largestNumber(
        [
            41,
            23,
            87,
            55,
            50,
            53,
            18,
            9,
            39,
            63,
            35,
            33,
            54,
            25,
            26,
            49,
            74,
            61,
            32,
            81,
            97,
            99,
            38,
            96,
            22,
            95,
            35,
            57,
            80,
            80,
            16,
            22,
            17,
            13,
            89,
            11,
            75,
            98,
            57,
            81,
            69,
            8,
            10,
            85,
            13,
            49,
            66,
            94,
            80,
            25,
            13,
            85,
            55,
            12,
            87,
            50,
            28,
            96,
            80,
            43,
            10,
            24,
            88,
            52,
            16,
            92,
            61,
            28,
            26,
            78,
            28,
            28,
            16,
            1,
            56,
            31,
            47,
            85,
            27,
            30,
            85,
            2,
            30,
            51,
            84,
            50,
            3,
            14,
            97,
            9,
            91,
            90,
            63,
            90,
            92,
            89,
            76,
            76,
            67,
            55,
        ]
    )
)
