# 274. H-Index
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # trivial case
        if len(citations) == 1:
            if citations[0] == 0:
                return 0
            else:
                return 1

        sorted_citations = sorted(citations)
        h_index = 0
        for i, j in enumerate(sorted_citations):
            if min(j, len(sorted_citations[i:])) < h_index:
                return h_index

            h_index = min(j, len(sorted_citations[i:]))

        return h_index


solution = Solution()
assert solution.hIndex([3, 0, 6, 1, 5]) == 3, "wrong"
assert solution.hIndex([1, 3, 1]) == 1, "wrong"
assert solution.hIndex([0, 1, 0]) == 1, "wrong"
assert solution.hIndex([0, 0]) == 0, "wrong"
assert solution.hIndex([1, 2]) == 1, "wrong"
assert solution.hIndex([11, 15]) == 2, "wrong"
assert solution.hIndex([0, 1]) == 1, "wrong"
