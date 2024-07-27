from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast, counter, prev = head, head, 0, head
        while fast:
            fast = fast.next
            counter += 1
            if counter > n:
                prev = slow
                slow = slow.next

        if n == counter:
            return head.next

        if slow:
            prev.next = slow.next

        else:
            prev.next = None

        return head
