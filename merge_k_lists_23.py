from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heads = [i for i in lists if i is not None]

        if not heads:
            return None

        merged = ListNode(float("-inf"))
        ans = merged

        while heads:
            min_node = ListNode(float("inf"))

            for i in heads:
                if i.val < min_node.val:
                    min_node = i

            heads.remove(min_node)
            merged.next = min_node
            merged = merged.next

            if min_node.next is not None:
                heads.append(min_node.next)

        return ans.next
