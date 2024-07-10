from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        head = root

        while head:
            prev_level = head
            prev_child = None
            level_start = None

            while prev_level:
                for child in (prev_level.left, prev_level.right):
                    if child:
                        if not level_start:
                            level_start = child

                        if prev_child:
                            prev_child.next = child

                        prev_child = child

                prev_level = prev_level.next
            head = level_start

        return root
