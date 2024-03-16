from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def sort(nums: List[int]) -> str:
            if len(nums) == 0:
                return ""
            elif len(nums) == 1:
                return str(nums[0])
            else:
                for i in range(0, len(nums)):
                    for j in range(i, len(nums)):
                        if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
                            nums[i], nums[j] = nums[j], nums[i]

                return "".join(nums)

        zeroes_ = ""
        nines_ = ""
        largest_number = ""

        numbers = {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            0: [],
        }

        for number in nums:
            if number == 0:
                zeroes_ += str(number)
            elif number == 9:
                nines_ += str(number)
            else:
                magnitude = len(str(number)) - 1
                index = number // (10**magnitude)
                numbers[index].append(str(number))

        for i in range(9, 0, -1):
            if len(numbers[i]) == 0:
                pass
            largest_number += str(sort(numbers[i]))

        return str(max((int(nines_ + largest_number + zeroes_)), 0))


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
