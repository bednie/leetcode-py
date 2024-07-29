from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        res = result = ListNode()
        node = head
        skip = [0] * 256

        while node:
            skip[node.val + 100] += 1
            node = node.next

        node = head
        while node:
            if skip[node.val + 100] == 1:
                res.next = node
                res = res.next
            node = node.next

        res.next = None

        return result.next
