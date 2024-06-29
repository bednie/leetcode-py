import itertools
from typing import List


class Solution:
    # one-liner
    # remember to redo this one
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations(range(1, n + 1), k)
