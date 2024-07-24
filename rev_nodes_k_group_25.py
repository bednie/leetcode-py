from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        stack = []
        pre = ListNode(val=-1, next=head)
        node = head
        start = pre
        
        while node:

            stack.append(node)
            node = node.next
            
            if len(stack) == k:  
                start.next = stack[-1]
                start = start.next
                stack[0].next = node
                while stack:
                    start.next = stack.pop()
                    start = start.next

        return pre.next