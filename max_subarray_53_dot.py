# leetcode 53: maximum subarray
# divide-and-conquer solution for CS-4050
# optionally generate graphviz dotfile
# Blair Ednie

from typing import List


class Solution:
    ##########################
    # graphviz
    # to generate png: dot -Tpng '/path/to/dotfile.dot' -o outfile.png     
    def __init__(self, debug=False):
        self.debug = debug
        self.debug_info = []
        self.node_count = 0

    def generate_dot_file(self):
        with open("debug_graph.dot", "w") as file:
            file.write(
                'digraph G {\n   \
                \tlabelloc="t";\n     \
                \tlabel="Visualization of Maximum Subarray Problem:\nDivide-and-Conquer Algorithm";\n   \
                \tfontsize=20;\n   \
                \tfontname="Helvetica";\n'
            )
            for info in self.debug_info:
                depth = info.get("depth", 0)
                label = f"bounds: {info['bounds']}, depth: {depth}, max: {info.get('max_sum', 'N/A')}"
                file.write(f'  node{info["id"]} [label="{label}"];\n')
                if info.get("parent") is not None:
                    file.write(f'  node{info["parent"]} -> node{info["id"]};\n')
            file.write("}\n")

    ##########################

    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide-and-Conquer Solution to find maximum contiguous subarray.
        """

        # trivial case
        if len(nums) == 1:
            return nums[0]

        # calculate max subarray crossing the middle index
        def maxSubArrayCrossing(
            nums: List[int], middle_index: int, lower_bound: int, upper_bound: int
        ) -> int:
            """
            Find max subarray across middle index of lower and upper bounds of array.
            """

            # iterate from middle to lower bound
            left_temp_sum = 0
            left_sum = -10_001  # initialize to be smaller than min(nums[i]) = -10**4
            for i in range(middle_index, (lower_bound - 1), -1):
                left_temp_sum += nums[i]
                if left_temp_sum > left_sum:
                    left_sum = left_temp_sum

            # iterate from middle to upper bound
            right_temp_sum = 0
            right_sum = -10_001  # initialize to be smaller than min(nums[i]) = -10**4
            for i in range(middle_index, (upper_bound + 1), 1):
                right_temp_sum += nums[i]
                if right_temp_sum > right_sum:
                    right_sum = right_temp_sum

            return (
                left_sum
                + right_sum
                - nums[middle_index]  # don't double count value at middle index
            )

        # divide array into left and right halves recursively
        def maxSubArrayRecursive(nums: List[int], lower_bound: int, upper_bound: int):
            """
            Divide array into left and right halves recursively.
            """

            # base case: length of nums is 1
            if lower_bound == upper_bound:
                max_sum = nums[lower_bound]
                ##########################
                # append info to graphviz
                if self.debug:
                    self.debug_info.append(
                        {
                            "id": node_id,
                            "action": "base",
                            "bounds": [lower_bound, upper_bound],
                            "max_sum": max_sum,
                            "depth": depth,
                            "parent": parent_id,
                        }
                    )
                ##########################

                return max_sum

            middle_index = (
                lower_bound + upper_bound
            ) // 2  # find middle_index using integer division

            ##########################
            # append info to graphviz
            self.debug_info.append(
                {
                    "id": node_id,
                    "action": "recurse",
                    "bounds": [lower_bound, upper_bound],
                    "max_sum": None,
                    "depth": depth,
                    "parent": parent_id,
                }
            )
            ##########################

            return max(
                maxSubArrayRecursive(nums, lower_bound, middle_index),  # left side
                maxSubArrayRecursive(
                    nums, (middle_index + 1), upper_bound
                ),  # right side
                maxSubArrayCrossing(
                    nums, middle_index, lower_bound, upper_bound
                ),  # crossing the middle
            )

        # initial recursive call
        result = maxSubArrayRecursive(nums, 0, len(nums) - 1)

        ##########################
        # graphviz
        if self.debug:
            self.generate_dot_file()
        ##########################

        return result


# testcases
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums2 = [
    84,
    87,
    78,
    16,
    94,
    36,
    87,
    93,
    50,
    22,
    63,
    28,
    91,
    60,
    64,
    27,
    41,
    27,
    73,
    37,
    12,
    69,
    68,
    30,
    83,
    31,
    63,
    24,
    68,
    36,
    30,
    3,
    23,
    59,
    70,
    68,
    94,
    57,
    12,
    43,
    30,
    74,
    22,
    20,
    85,
    38,
    99,
    25,
    16,
    71,
    14,
    27,
    92,
    81,
    57,
    74,
    63,
    71,
    97,
    82,
    6,
    26,
    85,
    28,
    37,
    6,
    47,
    30,
    14,
    58,
    25,
    96,
    83,
    46,
    15,
    68,
    35,
    65,
    44,
    51,
    88,
    9,
    77,
    79,
    89,
    85,
    4,
    52,
    55,
    100,
    33,
    61,
    77,
    69,
    40,
    13,
    27,
    87,
    95,
    40,
]
nums3 = [99]

solution = Solution()

print(nums)
print(f"Sum of max contiguous subarray: {solution.maxSubArray(nums)}")
assert solution.maxSubArray(nums) == 6, "Incorrect value for max subarray!"

print(nums2)
print(f"Sum of max contiguous subarray: {solution.maxSubArray(nums2)}")
assert solution.maxSubArray(nums2) == 5284, "Incorrect value for max subarray!"

print(nums3)
print(f"Sum of max contiguous subarray: {solution.maxSubArray(nums3)}")
assert solution.maxSubArray(nums3) == 99, "Incorrect value for max subarray!"
