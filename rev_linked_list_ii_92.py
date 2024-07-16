from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        l = head
        temp = []

        for i in range(1, right):
            if i >= left:
                temp.append(l)
            l = l.next

        left, right = 0, len(temp) - 1
        while left < right:
            temp[left].val, temp[right].val = temp[right].val, temp[left].val
            left += 1
            right -= 1

        return head
