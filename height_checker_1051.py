from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # trivial case
        if len(heights) == 1:
            return 0

        expected = sorted(heights)
        non_matching_indices = 0

        for i, j in zip(expected, heights):
            print(i, j)
            if i != j:
                non_matching_indices += 1

        return non_matching_indices


solution = Solution()
print(solution.heightChecker([1, 1, 4, 2, 1, 3]))
