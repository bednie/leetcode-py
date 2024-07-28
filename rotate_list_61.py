from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        pre, tail = ListNode(val=-999, next=head), None
        length = 1
        node = head
        while node.next:
            length += 1
            node = node.next
        
        tail = node

        k = k % length

        if k == 0 or length == 1:
            return head

        node, tail.next = head, head
        k_complement = length - k

        while k_complement > 1:
            node = node.next
            k_complement -= 1
            
        pre.next = node.next
        node.next = None
            
        return pre.next
        