from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle(node: Optional[ListNode]) -> tuple:
    slow, fast = node, node.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def merge(left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
    if not left:
        return right

    if not right:
        return left

    pre = ListNode(val=-999, next=None)
    tail = pre

    while left and right:
        if left.val < right.val:
            tail.next = left
            tail = tail.next
            left = left.next

        else:
            tail.next = right
            tail = tail.next
            right = right.next
        
    if left:
        tail.next = left

    if right:
        tail.next = right

    return pre.next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        l, mid = head, middle(head)
        r = mid.next
        mid.next = None

        left = self.sortList(l)
        right = self.sortList(r)

        return merge(left, right)