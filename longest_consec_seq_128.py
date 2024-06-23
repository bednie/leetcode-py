from typing import List


class Node:
    def __init__(self):
        self.low = None
        self.high = None


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        max_len = 0
        for i in nums:
            if i in seq:
                pass

            elif i - 1 in seq and i + 1 not in seq:
                seq[i] = seq[i - 1]
                seq[i].high = i

            elif i - 1 not in seq and i + 1 in seq:
                seq[i] = seq[i + 1]
                seq[i].low = i

            elif i - 1 in seq and i + 1 in seq:
                seq[i] = seq[i - 1]
                seq[i].high = seq[i + 1].high
                seq[seq[i].high] = seq[i]

            else:
                node = Node()
                node.high = i
                node.low = i
                seq[i] = node

            max_len = max(max_len, seq[i].high - seq[i].low + 1)

        return max_len
